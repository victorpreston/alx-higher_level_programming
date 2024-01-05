#!/bin/bash
# sends a POST request to the passed URL
curl -sL "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
