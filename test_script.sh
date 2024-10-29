#!/bin/bash
echo "Running without 'set -e':"
python3 test_exit.py
echo "This message appears if the shell does not stop on non-zero exit."
echo -e "\nRunning with 'set -e':"
set -e  # Enable exit on non-zero status
python3 test_exit.py
echo "This message will not appear if 'set -e' works as expected."
