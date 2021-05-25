#!/bin/bash
sudo mkdir -p /etc/systemd/system/docker.service.d
sudo cp http-proxy.conf /etc/systemd/system/docker.service.d/
sudo systemctl daemon-reload
sudo systemctl restart docker

