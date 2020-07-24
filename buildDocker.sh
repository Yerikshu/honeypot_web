#!/bin/bash
pip freeze > requirement
docker build -f ./Dockerfile-master . -t honeypot-master:latest
