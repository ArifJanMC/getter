#!/bin/bash

# Check if filename is provided
if [ -z "$1" ]; then
    echo "Usage: $0 <filename_or_path>"
    exit 1
fi

FILE_PATH=$1
FILE_NAME=$(basename "$FILE_PATH")
JUPYTER_SERVER="jup.arifjan.su"
JUPYTER_TOKEN="da6fced6df29a037c73ce1b0b58bbe730f4120469011cc57"  # Replace with your Jupyter Notebook token

# Read file content and encode it in base64
FILE_CONTENT=$(base64 "$FILE_PATH" | tr -d '\n')

# Create the JSON payload
JSON_PAYLOAD=$(jq -n --arg fc "$FILE_CONTENT" --arg fn "$FILE_NAME" '{"type": "file", "content": $fc, "format": "base64"}')

# Create the file on the Jupyter server
curl -X PUT "https://$JUPYTER_SERVER/api/contents/$FILE_NAME" \
     -H "Authorization: Token $JUPYTER_TOKEN" \
     -H "Content-Type: application/json" \
     -d "$JSON_PAYLOAD" \
     --insecure  # Remove this if your SSL certificate is properly configured
