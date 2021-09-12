import requests
import json

apiAddress = input('Origin: ')

parameters = {
        "key": "Vp56A7JqIHwIzdVknkaAjAaUrjOwbX0A",
        "location": apiAddress
    }

response = requests.get("http://www.mapquestapi.com/geocoding/v1/address", params=parameters)
data = response.text
dataJ = json.loads(data)['results']
ORG_lat = (dataJ[0]['locations'][0]['latLng']['lat'])
ORG_lng = (dataJ[0]['locations'][0]['latLng']['lng'])
print(ORG_lat,ORG_lng)


