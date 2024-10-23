#!/bin/bash
#set -xe
# Update packages
apt-get update
# Install required packages
apt-get install -y python3 python3-pip libpq-dev python3-dev python3.11-venv
# Create a virtual environment to manage Python packages
python3 -m venv venv
source venv/bin/activate
# Install the psycopg2 module in the virtual environment
pip install psycopg2-binary
