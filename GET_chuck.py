import requests
"""Test of api.chucknorris.io"""

url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print("Status code : " + str(result.status_code))

if result.status_code == 200:
    print("Success , we received new joke")
else:
    print("Failure, request not successful")
    result.encoding = 'utf-8'
print(result.text)
