import json
import requests


def post_Sample():
    App_URL = "https://reqres.in/api/users"
    addjson = open ('/home/kavin123/PycharmProjects/APITest/postaddjson.json','r')
    request_json = json.loads(addjson.read())
    response = requests.post(App_URL,request_json)
    print(response)

post_Sample()