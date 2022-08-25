import requests

response = requests.get("https://random-word-api.herokuapp.com/all")
print(response.text)