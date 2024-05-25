import sys
import os
import requests
import base64

# Check if filename is provided
if len(sys.argv) < 2:
    print("Usage: python script.py <filename_or_path>")
    sys.exit(1)

file_path = sys.argv[1]
file_name = os.path.basename(file_path)
jupyter_server = "jup.arifjan.su"
jupyter_token = "da6fced6df29a037c73ce1b0b58bbe730f4120469011cc57"  # Replace with your Jupyter Notebook token

# Read file content and encode it in base64
with open(file_path, 'rb') as file:
    file_content = base64.b64encode(file.read()).decode('utf-8')

# Create the file on the Jupyter server
url = f"https://{jupyter_server}/api/contents/{file_name}"
headers = {
    "Authorization": f"Token {jupyter_token}",
    "Content-Type": "application/json"
}
data = {
    "type": "file",
    "content": file_content,
    "format": "base64"
}

try:
    response = requests.put(url, headers=headers, json=data, verify=False)  # Set verify to True if you have a valid SSL certificate
    if response.status_code == 201:
        print(f"File {file_name} successfully created on the Jupyter server.")
    else:
        print(f"Failed to create file on the Jupyter server: {response.status_code} - {response.text}")
except requests.exceptions.RequestException as e:
    print(f"Error: {e}")
