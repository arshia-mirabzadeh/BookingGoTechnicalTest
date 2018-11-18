import sys
import requests
import json
import operator

#store url for each supplier
dave_url = 'https://techtest.rideways.com/dave'
eric_url = 'https://techtest.rideways.com/eric'
jeff_url = 'https://techtest.rideways.com/jeff'

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

	#check user input meets requirements
	check_user_input(sys.argv)

	#store user inputs
	pickup = sys.argv[1]
	dropoff = sys.argv[2]
	passengers = int(sys.argv[3])

	#initialise parameters for get requests
	parameters = {"pickup": pickup, "dropoff": dropoff}

	#call each supplier, ignore if no response within 2 secs
	try:
		dave_response = requests.get(dave_url, params=parameters, timeout=2)
		dave_data = json.loads(dave_response.text)
		dave_car_data = dave_data['options']
	except:
		pass
	try:
		eric_response = requests.get(dave_url, params=parameters, timeout=2)
		eric_data = json.loads(eric_response.text)
		eric_car_data = eric_data['options']
	except:
		pass
	try:
		jeff_response = requests.get(jeff_url, params=parameters, timeout=2)
		jeff_data = json.loads(jeff_response.text)
		jeff_car_data = jeff_data['options']
	except:
		pass

	#compute and store the best price and supplier for each available car type
	bestPrice = {}
	bestSupplier = {}

	if ('dave_car_data' in locals()):
		for item in dave_car_data:
			if (not capacity_satisfied(item['car_type'], passengers)):
				continue
			if (item['car_type'] in bestPrice.keys()):
				if (item['price'] < bestPrice.get(item['car_type'],'')):
					bestPrice[item['car_type']] = item['price']
					bestSupplier[item['car_type']] = 'Dave\'s Taxis'
			else:
				bestPrice[item['car_type']] = item['price']
				bestSupplier[item['car_type']] = 'Dave\'s Taxis'

	if ('jeff_car_data' in locals()):
		for item in jeff_car_data:
			if (not capacity_satisfied(item['car_type'], passengers)):
				continue
			if (item['car_type'] in bestPrice.keys()):
				if (item['price'] < bestPrice.get(item['car_type'],'')):
					bestPrice[item['car_type']] = item['price']
					bestSupplier[item['car_type']] = 'Jeff\'s Taxis'
			else:
				bestPrice[item['car_type']] = item['price']
				bestSupplier[item['car_type']] = 'Jeff\'s Taxis'

	if ('eric_car_data' in locals()):
		for item in eric_car_data:
			if (not capacity_satisfied(item['car_type'], passengers)):
				continue
			if (item['car_type'] in bestPrice.keys()):
				if (item['price'] < bestPrice.get(item['car_type'],'')):
					bestPrice[item['car_type']] = item['price']
					bestSupplier[item['car_type']] = 'Eric\'s Taxis'
			else:
				bestPrice[item['car_type']] = item['price']
				bestSupplier[item['car_type']] = 'Eric\'s Taxis'

	if (len(bestPrice) == 0):
		print ("No cars available")
		quit()

	#sort by price in decreasing order
	sortedPrices = sorted(bestPrice.items(), key=operator.itemgetter(1), reverse=True)

	#print results
	for item in sortedPrices:
		print (item[0], "-", bestSupplier.get(item[0],''), "-", item[1])