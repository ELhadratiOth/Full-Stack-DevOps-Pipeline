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

# Backend Firewall
resource "digitalocean_firewall" "backend_firewall" {
  name        = "backend-firewall"
  droplet_ids = [digitalocean_droplet.backend.id]

  inbound_rule {
    protocol         = "tcp"
    port_range       = "22"
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "8000"
    source_addresses = ["0.0.0.0/0", "::/0"]
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
    source_addresses = ["0.0.0.0/0", "::/0"]
  }

  inbound_rule {
    protocol         = "tcp"
    port_range       = "3000"
    source_addresses = ["0.0.0.0/0", "::/0"]
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


