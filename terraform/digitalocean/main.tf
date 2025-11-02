terraform {
  required_providers {
    digitalocean = {
      source  = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {
  token = var.digitalocean_token
}

# Jenkins Agent Firewall
resource "digitalocean_firewall" "jenkins_agent_firewall" {
  name        = "jenkins-agent-firewall"
  droplet_ids = [digitalocean_droplet.jenkins_agent.id]

  # SSH: allow only from Jenkins master (trusted IP)
  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = var.jenkins_master_ip != "" ? ["${var.jenkins_master_ip}/32"] : (var.trusted_ip != "" ? [var.trusted_ip] : ["0.0.0.0/0", "::/0"])
  }

  # Jenkins agent port (JNLP): allow connections ONLY from Jenkins controller/master
  inbound_rule {
    protocol         = "tcp"
    port_range       = "50000"
    source_addresses = var.jenkins_master_ip != "" ? ["${var.jenkins_master_ip}/32"] : ["0.0.0.0/0", "::/0"]
  }

  # Outbound: allow all traffic (agent needs to communicate with backend and frontend)
  outbound_rule {
    protocol              = "tcp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "udp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  tags = ["jenkins-agent"]
}

# Backend Firewall
resource "digitalocean_firewall" "backend_firewall" {
  name        = "backend-firewall"
  droplet_ids = [digitalocean_droplet.backend.id]

  # SSH: allow only the trusted IP if provided, otherwise keep open (use with caution)
  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = var.trusted_ip != "" ? [var.trusted_ip] : ["0.0.0.0/0", "::/0"]
  }

  # Application port: allow connections from the frontend droplet, Jenkins agent, and the trusted IP (if set).
  inbound_rule {
    protocol           = "tcp"
    port_range         = "8000"
    source_droplet_ids = [digitalocean_droplet.frontend.id, digitalocean_droplet.jenkins_agent.id]
    source_addresses   = var.trusted_ip != "" ? [var.trusted_ip] : []
  }

  outbound_rule {
    protocol              = "tcp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "udp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  tags = ["backend"]
}

# Frontend Firewall
resource "digitalocean_firewall" "frontend_firewall" {
  name        = "frontend-firewall"
  droplet_ids = [digitalocean_droplet.frontend.id]

  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = var.trusted_ip != "" ? [var.trusted_ip] : ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "3000"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  # Allow Jenkins agent to connect to frontend on port 3000 and SSH on port 22 (for deployments)
  inbound_rule {
    protocol           = "tcp"
    port_range         = "3000"
    source_droplet_ids = [digitalocean_droplet.jenkins_agent.id]
  }

  inbound_rule {
    protocol           = "tcp"
    port_range         = "22"
    source_droplet_ids = [digitalocean_droplet.jenkins_agent.id]
  }

  outbound_rule {
    protocol              = "tcp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  outbound_rule {
    protocol              = "udp"
    port_range            = "1-65535"
    destination_addresses = ["0.0.0.0/0", "::/0"]
  }

  tags = ["frontend"]
}

# PostgreSQL Managed Database
resource "digitalocean_database_cluster" "db" {
  name       = var.db_cluster_name
  engine     = "pg"
  version    = "16"
  region     = var.region
  node_count = 1
  size       = var.db_size
  tags       = ["postgres"]
}

# Backend Droplet
resource "digitalocean_droplet" "backend" {
  name     = "backend-droplet"
  region   = var.region
  size     = var.backend_size
  image    = var.image_slug
  backups  = false
  ipv6     = true
  ssh_keys = var.ssh_key_ids

  tags = ["backend"]

  depends_on = [
    digitalocean_database_cluster.db
  ]
}

# Frontend Droplet
resource "digitalocean_droplet" "frontend" {
  name     = "frontend-droplet"
  region   = var.region
  size     = var.frontend_size
  image    = var.image_slug
  backups  = false
  ipv6     = true
  ssh_keys = var.ssh_key_ids

  tags = ["frontend"]

  depends_on = [digitalocean_droplet.backend]
}

# Jenkins Agent Worker Droplet
resource "digitalocean_droplet" "jenkins_agent" {
  name     = "jenkins-agent-worker"
  region   = var.region
  size     = var.agent_size
  image    = var.image_slug
  backups  = false
  ipv6     = true
  ssh_keys = var.ssh_key_ids

  tags = ["jenkins-agent"]

  depends_on = [
    digitalocean_droplet.backend,
    digitalocean_droplet.frontend
  ]
}


