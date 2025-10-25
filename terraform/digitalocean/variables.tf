variable "digitalocean_token" {
  type      = string
  sensitive = true
}

variable "region" {
  type    = string
  default = "nyc3"
}

variable "image_slug" {
  type    = string
  default = "ubuntu-22-04-x64"
}

variable "backend_size" {
  type    = string
  default = "s-1vcpu-1gb"
}

variable "frontend_size" {
  type    = string
  default = "s-1vcpu-1gb"
}

variable "db_cluster_name" {
  type    = string
  default = "microservice-db"
}

variable "db_name" {
  type    = string
  default = "microservice_db"
}

variable "db_username" {
  type    = string
  default = "app_user"
}

variable "db_size" {
  type    = string
  default = "db-s-1vcpu-1gb"
}

variable "ssh_key_ids" {
  type        = list(string)
  description = "List of existing DigitalOcean SSH key IDs or fingerprints to attach to droplets"
  default     = []
}
