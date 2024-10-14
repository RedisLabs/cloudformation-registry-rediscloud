#!/bin/bash

# Update package list and install dependencies
sudo apt update
sudo apt install -y apt-transport-https ca-certificates curl software-properties-common

# Add Docker's GPG key
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

# Add Docker's APT repository
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Update package list to include Docker packages
sudo apt update

# Install Docker
sudo apt install -y docker-ce docker-ce-cli containerd.io

# Verify Docker installation
docker --version

# (Optional) Add current user to the docker group to use Docker as a non-root user
sudo usermod -aG docker $USER

# Print success message
echo "Docker installation completed. You may need to log out and log back in to use Docker as a non-root user."

# install jo
sudo apt-get install -y jq

# Install aws CLI
sudo apt install -y awscli