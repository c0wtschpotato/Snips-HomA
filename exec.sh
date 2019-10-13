#!/bin/bash
sudo git stash
sudo git pull
sudo systemctl restart snips-skill-server
sudo chmod +x action-MHZTrigger-HomA.py
sudo chmod +x action-hello-HomA.py