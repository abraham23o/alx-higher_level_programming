#!/bin/bash
# send a post request with a custom message and return a response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
