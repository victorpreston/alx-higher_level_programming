#!/bin/bash
#Displays all HTTP methods the server will accept
curl -sI "$1" | grep Allow | cut -d ' ' -f2-
