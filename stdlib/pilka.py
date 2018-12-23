import http.client
import json

connection = http.client.HTTPConnection('api.football-data.org')
headers = {'X-Auth-Token': '803329acbc354ae7a12f05610c56d6ab'}
connection.request('GET', '/v2/teams/86', None, headers)
response = json.loads(connection.getresponse().read().decode())

print(response)
