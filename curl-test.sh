#!/bin/bash

set -e

API_URL="http://localhost:5000/api/timeline_post"
RANDOM_ID="$(date +%s)"
TEST_NAME="Test User ${RANDOM_ID}"
TEST_EMAIL="test${RANDOM_ID}@example.com"
TEST_CONTENT="Automated timeline test ${RANDOM_ID}"

echo "Creating a random timeline post..."

POST_RESPONSE=$(curl --silent --show-error \
  --request POST "$API_URL" \
  --data-urlencode "name=$TEST_NAME" \
  --data-urlencode "email=$TEST_EMAIL" \
  --data-urlencode "content=$TEST_CONTENT")

echo "POST response:"
echo "$POST_RESPONSE"
echo

if [[ "$POST_RESPONSE" != *"$TEST_CONTENT"* ]]; then
  echo "POST test failed."
  exit 1
fi

echo "Checking the GET endpoint..."

GET_RESPONSE=$(curl --silent --show-error "$API_URL")

echo "GET response:"
echo "$GET_RESPONSE"
echo

if [[ "$GET_RESPONSE" == *"$TEST_CONTENT"* ]]; then
  echo "Success: the random timeline post was created and retrieved."
else
  echo "GET test failed: the new post was not found."
  exit 1
fi