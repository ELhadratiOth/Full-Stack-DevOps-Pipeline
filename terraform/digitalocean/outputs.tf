output "backend_ip" {
  value = try(digitalocean_floating_ip.backend_ip.ip_address, null)
}

output "frontend_ip" {
  value = try(digitalocean_floating_ip.frontend_ip.ip_address, null)
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
  value = try("http://${digitalocean_floating_ip.frontend_ip.ip_address}:3000", null)
}

output "backend_url" {
  value = try("http://${digitalocean_floating_ip.backend_ip.ip_address}:8000", null)
}
