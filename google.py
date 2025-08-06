import requests

respose = requests.get('https://google.com')

print(respose.text)