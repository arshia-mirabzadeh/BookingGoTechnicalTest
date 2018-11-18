import sys
import requests
import json
import operator

dave_url = 'https://techtest.rideways.com/dave'

#function to check if a car type can fit the number of passengers
def capacity_satisfied(car_type, passengers):
	if ((car_type == 'STANDARD' or car_type == 'EXECUTIVE' or car_type == 'LUXURY') and passengers <= 4):
		return True
	if ((car_type == 'PEOPLE_CARRIER' or car_type == 'LUXURY_PEOPLE_CARRIER') and passengers <= 6):
		return True
	if (car_type == 'MINIBUS' and passengers <= 16):
		return True
	return False

def check_user_input(arguments):

	#check length of supplied args
	if (len(arguments) != 4):
		raise ValueError("Please specify correct arguments: ./BookingGo.py [Pickup] [Dropoff] [No of Passenger]")

	#check formatting of pickup/dropoff
	if (',' not in arguments[1] or ',' not in arguments[2]):
		raise ValueError("Please specify pickup and dropoff in the format: <lat,lon>")

	#check latitude and longitudes are numbers
	try:
		temp = float(arguments[1].split(',')[0])
		temp = float(arguments[1].split(',')[1])
		temp = float(arguments[2].split(',')[0])
		temp = float(arguments[2].split(',')[1])
	except:
		raise ValueError("Please specify your pickup/dropoff latitudes and longitudes as numbers")

	#check latitudes and longitudes are within range
	lat1 = float(arguments[1].split(',')[0])
	lat2 = float(arguments[2].split(',')[0])
	lon1 = float(arguments[1].split(',')[1])
	lon2 = float(arguments[2].split(',')[1])

	if (lat1 < -90.0 or lat2 < -90.0 or lat1 > 90.0 or lat2 > 90.0):
		raise ValueError("Latitude Values are out of range (-90 to 90)")
	if (lon1 < -180.0 or lon2 < -180.0 or lon1 > 180.0 or lon2 > 180.0):
		raise ValueError("Longitude Values are out of range (-180 to 180)")

	#check passenger number field is a number
	try:
		temp = int(arguments[3])
	except:
		raise ValueError("Please specify the number of passengers as an integer")

	#check number of passengers is valid
	if (int(arguments[3]) < 1 or int(arguments[3]) > 16):
		raise ValueError("Please specify a number of passengers between 1 and 16")

if __name__ == "__main__":

	check_user_input(sys.argv)
	
	#store passed arguments
	pickup = sys.argv[1]
	dropoff = sys.argv[2]
	passengers = int(sys.argv[3])

	parameters = {"pickup": pickup, "dropoff": dropoff}

	try:
		dave_response = requests.get(dave_url, params=parameters, timeout=2)
	except:
		print ("Dave's Taxis did not respond in time")
		quit()

	if (dave_response.status_code != 200):
		print ("Invalid request/Internal Server Error")
		print ("Check parameters and try again")
		quit()

	dave_data = json.loads(dave_response.text)
	dave_car_data = dave_data['options']

	newDict = {}

	for item in dave_car_data:
		if (capacity_satisfied(item['car_type'], passengers)):
			newDict[item['car_type']] = item['price']

	if (len(newDict) == 0):
		print ("No cars available")
		quit()

	sortedDict = sorted(newDict.items(), key=operator.itemgetter(1), reverse=True)

	for item in sortedDict:
			print (item[0], " - Dave's Taxis - ",  item[1])