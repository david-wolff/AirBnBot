import requests
import geocoder
import json

g = geocoder.ip('me')
lat = g.latlng[0]
lng = g.latlng[1]


MAPS_API_KEY = 'AIzaSyBumUG1oL-ZxmO6v2f2McFmdUC3Fx5Z7Pk'

payload={}
headers={}
url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={}%2C{}&radius=150000&type=restaurant&keyword=cruise&key={}".format(lat,lng,MAPS_API_KEY)

response = requests.request("GET", url, headers=headers, data=payload)

with open('outputfile.json', 'wb') as outfile:
    outfile.write(response.content)

places_file = open('/Users/davidwolff/airbnbot/outputfile.json')
places_data = json.load(places_file)
number_of_places = len(places_data["results"])
list_of_places = []
i = 0
while i < number_of_places:
    list_of_places.append(places_data["results"][i]["name"])  
    list_of_places.append(places_data["results"][i]["vicinity"])
    i += 1
print(list_of_places)


