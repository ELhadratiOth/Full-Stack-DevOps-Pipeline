# Ansible Playbooks

## Structure

```
playbooks/
├── site.yml          # Master playbook (runs all)
├── frontend.yml      # Frontend VM provisioning
└── backend.yml       # Backend VM provisioning
```

## Installed Software

### Frontend VM

- **Node.js 20.x** (with npm)
- **Global packages**: pm2, yarn
- **Docker** (latest)
- **Nginx** (web server/reverse proxy)
- Essential tools: git, curl, wget, vim, htop

### Backend VM

- **Python 3.11** (with pip)
- **Python packages**: virtualenv, pipenv, gunicorn, uvicorn
- **Docker** (latest)
- **PostgreSQL client** (for database connections)
- Essential tools: git, curl, wget, vim, htop, monitoring tools

## Usage

### Run all playbooks:

```bash
ansible-playbook -i ../inventory/hosts.yml site.yml
```

### Run only frontend:

```bash
ansible-playbook -i ../inventory/hosts.yml site.yml --tags frontend
# OR
ansible-playbook -i ../inventory/hosts.yml frontend.yml
```

### Run only backend:

```bash
ansible-playbook -i ../inventory/hosts.yml site.yml --tags backend
# OR
ansible-playbook -i ../inventory/hosts.yml backend.yml
```

### Run specific components:

```bash
# Install only Docker on both VMs
ansible-playbook -i ../inventory/hosts.yml site.yml --tags docker

# Setup only firewall rules
ansible-playbook -i ../inventory/hosts.yml site.yml --tags firewall

# Install only Node.js on frontend
ansible-playbook -i ../inventory/hosts.yml frontend.yml --tags nodejs
```

### Check mode (dry run):

```bash
ansible-playbook -i ../inventory/hosts.yml site.yml --check
```

### Verbose output:

```bash
ansible-playbook -i ../inventory/hosts.yml site.yml -v
# or -vv, -vvv for more verbosity
```

## Optimization Features

1. **Idempotent**: Can run multiple times safely
2. **Conditional execution**: Checks if software already installed
3. **Tags**: Run specific parts only
4. **Caching**: APT cache valid for 1 hour
5. **Parallel execution**: Runs tasks in parallel where possible
6. **Handlers**: Services restarted only when needed
7. **Performance tuning**: Swap disabled, system limits configured

## Firewall Configuration

### Frontend (Port 3000):

- SSH (22)
- HTTP (80)
- HTTPS (443)
- Node.js app (3000)

### Backend (Port 8000):

- SSH (22)
- API (8000)

## Environment Configuration

Backend VM includes a `.env.example` template at `/opt/backend/.env.example` with:

- Database connection settings
- Application configuration

Copy and customize:

```bash
cp /opt/backend/.env.example /opt/backend/.env
# Edit with your actual values
```
