output "backend_ip" {
  value = digitalocean_droplet.backend.ipv4_address
}

output "frontend_ip" {
  value = digitalocean_droplet.frontend.ipv4_address
}

output "db_host" {
  value = digitalocean_database_cluster.db.host
}

output "db_port" {
  value = digitalocean_database_cluster.db.port
}

output "db_name" {
  value = var.db_name
}

output "db_username" {
  value = var.db_username
}

output "frontend_url" {
  value = "http://${digitalocean_droplet.frontend.ipv4_address}:3000"
}

output "backend_url" {
  value = "http://${digitalocean_droplet.backend.ipv4_address}:8000"
}

output "jenkins_agent_ip" {
  value       = digitalocean_droplet.jenkins_agent.ipv4_address
  description = "IP address of the Jenkins agent worker droplet for SSH configuration"
}
