import sys
import requests
import json
import operator

url = 'http://localhost:8080/'

if (len(sys.argv) != 4):
		print ("Please specify correct arguments: ./BookingGo.py [Pickup] [Dropoff] [No of Passenger]")
		quit()

parameters = {"pickup": sys.argv[1], "dropoff": sys.argv[2], "passengers": sys.argv[3]}

try:
	response = requests.get(url, params=parameters)
except:
	print ("Connection could not be made. Check server is running and url/parameters are correct")
	quit()

if (response.status_code == 200):
	data = json.loads(response.text)
	for item in data:
		print (item['car_type'], "-", item['supplier'], "-", item['price'])
else:
	if (response.status_code == 204):
		print ("No cars available. Try again later")
	else:
		print (response.text)
