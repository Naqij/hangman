import random
import requests

response = requests.get("https://random-word-api.herokuapp.com/all")
print(response.text)

#import random word using API
#input user word choice
#5 lives