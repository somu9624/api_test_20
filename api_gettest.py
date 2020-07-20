import requests
import jsonpath

def get():
    details = "https://reqres.in/api/users/2"
    response = requests.get (details)
    assert response.status_code == 200
    if response.status_code == 200:
        print("Success")
    else:
        print("Failure")
    print(response.text)

    abc = jsonpath.jsonpath(response.json(),'data.id')
    if abc[0] == 2:
        print ("Assertion Passed")
    else:
        print("Assertion Failed")

    abc = response.json()
    print(abc['data'])

get()