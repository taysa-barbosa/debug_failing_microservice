#!/bin/bash

set -e

cd /app

# Fix dependency conflict
sed -i 's/requests==2.25.0/requests==2.31.0/' requirements.txt

# Install dependencies
pip install --no-cache-dir -r requirements.txt

# Set Redis host
export REDIS_HOST=localhost

# Run app (basic validation)
python app.py &
sleep 3

# Check if app is responding
curl -s http://localhost:5000 | grep "App is running"
