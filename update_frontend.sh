#!/bin/bash
set -e

# Configuration
# The folder where you keep your git clone of the frontend
REPO_DIR="/opt/workmatch_frontend_repo" 
# The web root where Nginx serves files
WEB_ROOT="/var/www/html"                

echo "--- Starting Frontend Update ---"

# 1. Pull latest code from Git
echo "Pulling latest code from Git..."
cd "$REPO_DIR"
git pull origin main

# 2. Sync files to Nginx web root
# We exclude .git and other helper scripts to keep production clean
echo "Syncing files to $WEB_ROOT..."
sudo rsync -av --delete \
    --exclude='.git' \
    --exclude='.gitignore' \
    --exclude='*.py' \
    --exclude='*.log' \
    "$REPO_DIR/" "$WEB_ROOT/"

# 3. Fix permissions
# www-data is the standard user for Nginx on Ubuntu
echo "Updating permissions..."
sudo chown -R www-data:www-data "$WEB_ROOT"
sudo find "$WEB_ROOT" -type d -exec chmod 755 {} \;
sudo find "$WEB_ROOT" -type f -exec chmod 644 {} \;

# 4. Restart Nginx to apply any changes
echo "Restarting Nginx..."
sudo systemctl restart nginx

echo "--- Frontend Update Complete! ---"
