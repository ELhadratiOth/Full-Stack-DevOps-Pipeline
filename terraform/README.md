# Terraform Infrastructure as Code

Infrastructure management for DigitalOcean using Terraform.

## Overview

This directory contains Terraform configurations for deploying and managing cloud infrastructure on DigitalOcean, including:

- **Droplets (VMs)**: Backend API server and Frontend web server
- **Managed Database**: PostgreSQL database cluster
- **Firewall Rules**: Network security with IP-based access control
- **Networking**: VPC and internal communication

## Directory Structure

```
terraform/
├── digitalocean/              # DigitalOcean provider configuration
│   ├── main.tf               # Primary resource definitions
│   ├── variables.tf          # Input variable definitions
│   ├── outputs.tf            # Output values
│   ├── terraform.tfvars      # Variable defaults
│   ├── secret.auto.tfvars    # Local secrets (NOT in git)
│   └── .terraform/           # Terraform state and plugins
```

## Security Configuration

### Firewall Rules (DigitalOcean)

The infrastructure uses a security model that restricts backend access to authorized sources only.

#### Backend API (Port 8000)

**Inbound Rules:**

- **SSH (Port 22)**: Restricted to your personal machine's public IP
- **HTTP (Port 8000)**: Allowed from:
  - Frontend droplet (internal DigitalOcean network)
  - Your personal machine (via trusted_ip variable)

#### Frontend (Port 3000)

**Inbound Rules:**

- **SSH (Port 22)**: Restricted to your personal machine's public IP
- **HTTP (Port 3000)**: Open to all (public facing application)

### Trusted IP Configuration

The `trusted_ip` variable controls access from your personal machine:

```hcl
variable "trusted_ip" {
  type        = string
  description = "Your personal public IP for firewall rules"
  default     = ""
}
```

#### Updating Your Trusted IP

**Step 1: Discover your current public IP**

```bash
# Windows PowerShell
Invoke-RestMethod https://ipinfo.io/ip

# Linux/Mac
curl https://ipinfo.io/ip
```

**Step 2: Update the local secrets file**

Edit `terraform/digitalocean/secret.auto.tfvars`:

```hcl
trusted_ip = "YOUR.PUBLIC.IP/32"
```

**Note:** This file is in `.gitignore` and not committed to version control.

**Step 3: Apply the firewall changes**

```bash
cd terraform/digitalocean
terraform plan -var-file=secret.auto.tfvars
terraform apply -var-file=secret.auto.tfvars
```

### Security Benefits

- **Backend Isolation**: API is not publicly accessible
- **Controlled Access**: Only authorized IPs can SSH into VMs
- **Network Segregation**: Frontend and backend communicate internally
- **Secret Management**: Sensitive IPs stored locally, not in git

## Prerequisites

- Terraform >= 1.0
- DigitalOcean account with API token
- `doctl` (optional, for additional DigitalOcean operations)

## Environment Setup

### Create DigitalOcean API Token

1. Visit [DigitalOcean Console](https://cloud.digitalocean.com)
2. Navigate to Settings → API → Tokens
3. Generate a new Personal Access Token
4. Save it securely (you'll only see it once)

### Configure Terraform

Set the DigitalOcean token as an environment variable:

**Windows PowerShell:**

```powershell
$env:DIGITALOCEAN_TOKEN = "your_api_token_here"
```

**Linux/Mac:**

```bash
export DIGITALOCEAN_TOKEN="your_api_token_here"
```

## Common Terraform Commands

### Initialize Terraform

```bash
cd terraform/digitalocean
terraform init
```

This downloads required providers and initializes the working directory.

### Plan Infrastructure Changes

```bash
terraform plan -var-file=secret.auto.tfvars
```

Shows what changes will be made without applying them.

### Apply Infrastructure Changes

```bash
terraform apply -var-file=secret.auto.tfvars
```

Creates or modifies infrastructure based on configuration.

### Destroy Infrastructure

```bash
terraform destroy -var-file=secret.auto.tfvars
```

⚠️ **Warning**: This will delete all managed resources.

### View Output Values

```bash
terraform output -json
```

Shows deployed infrastructure details (IPs, hostnames, etc.).

### Refresh State

```bash
terraform refresh -var-file=secret.auto.tfvars
```

Updates state file with current resource status.

## Configuration Files

### main.tf

Contains resource definitions:

- **Droplets**: Backend and Frontend VMs
- **Database**: Managed PostgreSQL cluster
- **Firewall**: Inbound/outbound rules for both VMs
- **DNS**: Optional DNS record configuration

### variables.tf

Defines input variables:

- `region`: DigitalOcean region (default: "nyc3")
- `trusted_ip`: Your personal public IP (loaded from secret.auto.tfvars)
- `database_name`: PostgreSQL database name
- `droplet_size`: VM size and resources

### outputs.tf

Exports important values after deployment:

- Backend VM IP address
- Frontend VM IP address
- Database connection string
- Firewall rule IDs

### terraform.tfvars

Default variable values (committed to git).

### secret.auto.tfvars

**Local-only file containing:**

```hcl
trusted_ip = "YOUR.IP/32"
```

## Troubleshooting

### Terraform Can't Connect to DigitalOcean

**Error:** `Error: Unauthorized: Token is invalid`

**Solution:**

```bash
# Verify token is set
echo $env:DIGITALOCEAN_TOKEN  # Windows
echo $DIGITALOCEAN_TOKEN       # Linux/Mac

# Ensure token has proper permissions in DigitalOcean Console
```

### Firewall Rules Not Updating

**Solution:**

```bash
# Refresh Terraform state
terraform refresh -var-file=secret.auto.tfvars

# Check current configuration
terraform show

# Reapply if needed
terraform apply -var-file=secret.auto.tfvars
```

### SSH Access Still Restricted After Firewall Update

**Possible causes:**

- Your public IP changed (ISP rotation)
- Firewall rules not applied yet

**Solution:**

1. Verify your current IP: `Invoke-RestMethod https://ipinfo.io/ip`
2. Update `secret.auto.tfvars` with new IP
3. Reapply: `terraform apply -var-file=secret.auto.tfvars`
4. Wait 1-2 minutes for rules to take effect

### State File Corruption

**Solution:**

```bash
# Backup current state
cp terraform.tfstate terraform.tfstate.backup

# Refresh from actual resources
terraform refresh -var-file=secret.auto.tfvars
```
