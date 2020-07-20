import requests

details = "https://reqres.in/api/users/2"
response = requests.get (details)
print(response.text)