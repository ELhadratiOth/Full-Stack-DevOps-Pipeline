# Quick Commands Reference

## Ansible Container

### Connect to Ansible container

docker exec -it ansible /bin/bash

### Start Ansible services

cd ansible
docker compose up -d

### Stop Ansible services

cd ansible
docker compose down

### Rebuild and start Ansible

cd ansible
docker compose up -d --build

### Run backend playbook

ansible-playbook -i ../inventory/hosts.yml backend.yml

### Run frontend playbook

ansible-playbook -i ../inventory/hosts.yml frontend.yml

### Run all playbooks

ansible-playbook -i ../inventory/hosts.yml site.yml

### Run Jenkins agent playbook

ansible-playbook -i ../inventory/hosts.yml jenkins_agent.yml

### Run Jenkins agent with specific tags

ansible-playbook -i ../inventory/hosts.yml jenkins_agent.yml --tags docker
ansible-playbook -i ../inventory/hosts.yml jenkins_agent.yml --tags ssh
ansible-playbook -i ../inventory/hosts.yml jenkins_agent.yml --tags java

## Jenkins Container

### Connect to Jenkins container

docker exec -it jenkins /bin/bash

### Start Jenkins services

cd jenkins
docker compose up -d

### Stop Jenkins services

cd jenkins
docker compose down

### Rebuild and start Jenkins

cd jenkins
docker compose up -d --build

# IP Address Retrieval

## Get Public IP of Backend Server

```bash
Invoke-RestMethod https://ipinfo.io/ip
```
