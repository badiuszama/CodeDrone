import openrouteservice as ors
import folium
#import GDest, geocodeing_2

ors_key = '5b3ce3597851110001cf62486905683bd4754a8c8c22017f27414546'

###################### Origin lat&lng
#print(geocodeing_2.ORG_lat,geocodeing_2.ORG_lng)
##################### Destination lat&lng
#print(GDest.DST_lat, GDest.DST_lng)
#######################
#coordinates = [[geocodeing_2.ORG_lng, geocodeing_2.ORG_lat], [GDest.DST_lng, GDest.DST_lat]]
coordinates = [[-86.781247, 36.163532], [-80.191850, 25.771645]]
client = ors.Client(key=ors_key)
route = client.directions(coordinates=coordinates,
                          profile='driving-car',
                          format='geojson')
map_directions = folium.Map(location=[33.77, -84.37], zoom_start=5)
folium.GeoJson(route, name='route').add_to(map_directions)
folium.LayerControl().add_to(map_directions)
map_directions
print(route['features'][0]['properties']['segments'][0]['distance'], 'miles')
print(route['features'][0]['properties']['segments'][0]['duration'], 'hours\n')
print('directions')
for index, i in enumerate(route['features'][0]['properties']['segments'][0]['steps']):
    print(index+1, i, '\n')

