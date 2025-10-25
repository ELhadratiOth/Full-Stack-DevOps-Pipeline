# DigitalOcean Setup - 3 Steps

## Step 1: Get Token

1. Go to: https://cloud.digitalocean.com/account/api/tokens
2. Click "Generate New Token"
3. Name it "terraform"
4. Select: Read + Write scopes
5. Copy the token

## Step 2: Configure & Deploy

```bash
cd terraform/digitalocean

# Copy example config
cp terraform.tfvars.example terraform.tfvars

# Edit with your token
nano terraform.tfvars
# Set: digitalocean_token = "dop_v1_..."
# Also update GitHub URLs in backend_init.sh and frontend_init.sh

# Deploy
terraform init
terraform plan
terraform apply  # Type: yes
```

## Step 3: Get Your URLs

```bash
terraform output

# You'll get:
# frontend_ip = 198.51.100.50
# backend_ip = 192.0.2.100
#
# Access:
# Frontend: http://198.51.100.50:3000
# API: http://192.0.2.100:8000/docs
```

**That's it! Everything is configured automatically.**

See `HOW_CREDENTIALS_SHARED.md` for how credentials work.
