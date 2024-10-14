#!/usr/bin/env bash

docker run -d -p 4444:4444 --shm-size="2g" selenium/standalone-chrome:4.25.0-20240922
