import requests

r = requests.get('http://swapi.co/api/people/1')
print r.json()
