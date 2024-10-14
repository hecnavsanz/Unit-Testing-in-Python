#!/usr/bin/env bash

sudo dnf config-manager --add-repo https://download.docker.com/linux/centos/docker-ce.repo

sudo dnf -y install docker-ce docker-ce-cli containerd.io docker-compose-plugin

sudo usermod -aG docker labs

sudo systemctl enable --now docker

sudo systemctl status docker --no-pager
