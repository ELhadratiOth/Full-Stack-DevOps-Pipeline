FROM python:3.11-slim

# Set metadata
LABEL maintainer="Othman <othmanelhadrati@gmail.com>"
LABEL description="Ansible control node container"

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        sshpass \
        openssh-client \
        curl \
        git \
        vim && \
    pip install --no-cache-dir ansible && \
    rm -rf /var/lib/apt/lists/*

# Set work directory
WORKDIR /ansible

# Create entrypoint script to copy and fix SSH permissions
RUN echo '#!/bin/bash\n\
if [ -d /tmp/ssh-keys ]; then\n\
  mkdir -p /root/.ssh\n\
  cp -r /tmp/ssh-keys/* /root/.ssh/ 2>/dev/null || true\n\
  chmod 700 /root/.ssh\n\
  find /root/.ssh -type f -name "id_*" ! -name "*.pub" -exec chmod 600 {} \;\n\
  find /root/.ssh -type f -name "*.pub" -exec chmod 644 {} \;\n\
  touch /root/.ssh/known_hosts\n\
  chmod 644 /root/.ssh/known_hosts\n\
fi\n\
exec "$@"' > /entrypoint.sh && chmod +x /entrypoint.sh

ENTRYPOINT ["/entrypoint.sh"]
CMD ["/bin/bash"]
