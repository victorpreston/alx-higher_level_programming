#!/bin/bash
# send a request and displays only the status code of the response
curl -s -o /dev/null -I --w "%{http_code}" "$1"
