#!/bin/bash
# Script that takes in a URL, sends a request and displays
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
