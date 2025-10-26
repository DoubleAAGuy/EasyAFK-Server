import requests

# URL of the Flask endpoint
url = "http://127.0.0.1:80/process"

# Data to send
data = "b'steve, localhost/127.0.0.1:25565'"

# Send POST request with JSON
response = requests.post(url, json=data)

# Print the response from the server
if response.status_code == 200:
    print("Server response:", response.content.decode('utf-8'))  # No parentheses here
else:
    print("Error:", response.status_code, response.text)
