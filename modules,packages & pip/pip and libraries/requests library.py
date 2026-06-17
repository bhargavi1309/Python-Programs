#pip install requests is a command to install requests library in python.
import requests

response = requests.get(
    "https://example.com"
)

print(response.status_code)
#output will be 200 if the request is successful, otherwise it will return an error code.