import urllib.request
import json
api_key = 'Vp56A7JqIHwIzdVknkaAjAaUrjOwbX0A'
endpoint = 'http://www.mapquestapi.com/directions/v2/route?'
origin = input('Where are you?: ').replace(' ', '+')
destination = input('Where do you want to go?: ').replace(' ', '+')
#nav_request = 'origin={}&destination={}&key={}'.format(origin,destination,api_key)
nav_request = 'Key={}&origin={}&destination={}'.format(api_key, origin, destination)
request = endpoint + nav_request
response = urllib.request.urlopen(request).read()
directions = json.loads(response)
print(directions)