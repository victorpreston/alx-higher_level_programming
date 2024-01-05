#!/bin/bash
# send a POST request with the contents of a file
curl -s -H "content-type:application/json"  -d @"$2" -X POST "$1"
