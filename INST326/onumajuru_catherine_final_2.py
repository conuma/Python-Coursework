import pickle
import requests
import json
import xml.etree.ElementTree
API = "u7jXXi3j81vGghZCIoU2nNt3aTC3oWUK"
fh = open("onumajuru_catherine_cities.txt", 'rb')
cities = pickle.load(fh)
city_list = []
for i in cities:
    place = i.split('\t')
    location = place[0]
    count = place[1]
    #city_list.append(location)
    url = "http://open.mapquestapi.com/geocoding/v1/address?&key=" + API + "&location=" + location
    data = requests.get(url)
    result = json.loads(data.text)
    lat = result['results'][0]['locations'][0]['latLng']['lat']
    long = result['results'][0]['locations'][0]['latLng']['lng']
    print("Lat: " + str(lat) + ", " + "Lon: " + str(long) + ": " + str(count) + " UFO Sightings")