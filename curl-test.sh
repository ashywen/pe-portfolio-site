#!/bin/bash

BASE_URL="http://127.0.0.1:5000"

NAME="TestUser$(date +%s)"
EMAIL="test$(date +%s)@example.com"
CONTENT="Automated curl test"

echo "Creating timeline post..."

POST_RESPONSE=$(curl -s -X POST "$BASE_URL/api/timeline_post" \
-H "Content-Type: application/x-www-form-urlencoded" \
-d "name=$NAME&email=$EMAIL&content=$CONTENT")

echo "POST response:"
echo $POST_RESPONSE


echo ""
echo "Checking timeline posts..."

GET_RESPONSE=$(curl -s "$BASE_URL/api/timeline_post")

echo "GET response:"
echo $GET_RESPONSE


if [[ "$GET_RESPONSE" == *"$CONTENT"* ]]; then
    echo "SUCCESS: Timeline post was added!"
    exit 0
else
    echo "FAILURE: Timeline post was not found!"
    exit 1
fi