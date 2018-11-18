var express = require('express'),
    request = require('request'),
    app = express(),
    port = process.env.PORT || 8080,
    Dict = require("collections/dict");

const capacity_satisfied = function capacity_satisfied(car_type, passengers)
{
	if ((car_type == 'STANDARD' || car_type == 'EXECUTIVE' || car_type == 'LUXURY') && passengers <= 4)
		return true
	if ((car_type == 'PEOPLE_CARRIER' || car_type == 'LUXURY_PEOPLE_CARRIER') && passengers <= 6)
		return true
	if (car_type == 'MINIBUS' && passengers <= 16)
		return true
	return false
}

const check_arguments = function check_arguments(pickup, dropoff, passengers)
{
	//check parameters are present
	if (pickup == null || dropoff == null || passengers == null)
		return "3 Parameters required. pickup=lat,lon dropoff=lat,lon passengers=<1-16>";

	//check pickup format
	if (!pickup.includes(",", 0))
		return "Pickup must be in format: lat,lon. for example 3.42,-50.65"

	//check dropoff format
	if (!dropoff.includes(",", 0))
		return "Dropoff must be in format: lat,lon. for example 3.42,-50.65"

	var lat1 = pickup.split(",")[0];
	var lon1 = pickup.split(",")[1];
	var lat2 = dropoff.split(",")[0];
	var lon2 = dropoff.split(",")[1];

	//check passed co-ordinates are numbers
	if (isNaN(lat1) || isNaN(lon1))
		return "Pickup co-ordinates must be numbers"

	if (isNaN(lat2) || isNaN(lon2))
		return "Dropoff co-ordinates must be numbers"

	//check latitudes and longitudes are within range
	if (lat1 < -90.0 || lat2 < -90.0 || lat1 > 90.0 || lat2 > 90.0)
		return "Latitude values are out of range. Latitude should be between -90 and 90"

	if (lon1 < -180.0 || lon2 < -180.0 || lon1 > 180.0 || lon2 > 180.0)
		return "Longitude values are out of range. Longitude should be between -180 and 180"

	//check passenger value is an integer
	if (isNaN(passengers))
		return "passengers parameter must be an integer"

	var temp = Number(passengers)
	if (!Number.isInteger(temp))
		return "passengers parameter must be an integer between 1 and 16"

	//check passenger value is within range
	if (passengers < 1 || passengers > 16)
		return "number of passengers must be between 1 and 16"

	return true;
}

var callDave = function callDave(pickup, dropoff, passengers, bestPrice, bestSupplier, callback)
{
	var parameters = {url: 'https://techtest.rideways.com/dave', qs: {pickup: pickup, dropoff: dropoff}, timeout: 2000};
	request(parameters, function(error, response, body)
	{
		if (error || response.statusCode == 500)
		{
			callback();
		}
		else
		{
			var json = JSON.parse(body);

			for (var i = 0; i < json.options.length; i++)
			{
				if (capacity_satisfied(json.options[i].car_type, passengers))
				{
					if (bestPrice.has(json.options[i].car_type))
					{
						if (json.options[i].price < bestPrice.get(json.options[i].car_type))
						{
							bestPrice.set(json.options[i].car_type, json.options[i].price);
							bestSupplier.set(json.options[i].car_type, 'Dave\'s Taxis');
						}
					}
					else
					{
						bestPrice.set(json.options[i].car_type, json.options[i].price);
						bestSupplier.set(json.options[i].car_type, 'Dave\'s Taxis');
					}
				}
			}
			callback();
		}
	})
}

var callEric = function callEric(pickup, dropoff, passengers, bestPrice, bestSupplier, callback)
{
	var parameters = {url: 'https://techtest.rideways.com/eric', qs: {pickup: pickup, dropoff: dropoff}, timeout: 2000};
	request(parameters, function(error, response, body)
	{
		if (error || response.statusCode == 500)
		{
			callback();
		}
		else
		{
			var json = JSON.parse(body);

			for (var i = 0; i < json.options.length; i++)
			{
				if (capacity_satisfied(json.options[i].car_type, passengers))
				{
					if (bestPrice.has(json.options[i].car_type))
					{
						if (json.options[i].price < bestPrice.get(json.options[i].car_type))
						{
							bestPrice.set(json.options[i].car_type, json.options[i].price);
							bestSupplier.set(json.options[i].car_type, 'Eric\'s Taxis');
						}
					}
					else
					{
						bestPrice.set(json.options[i].car_type, json.options[i].price);
						bestSupplier.set(json.options[i].car_type, 'Eric\'s Taxis');
					}
				}
			}
			callback();
		}
	})
}

var callJeff = function callJeff(pickup, dropoff, passengers, bestPrice, bestSupplier, callback)
{
	var parameters = {url: 'https://techtest.rideways.com/jeff', qs: {pickup: pickup, dropoff: dropoff}, timeout: 2000};
	request(parameters, function(error, response, body)
	{
		if (error || response.statusCode == 500)
		{
			callback();
		}
		else
		{
			var json = JSON.parse(body);

			for (var i = 0; i < json.options.length; i++)
			{
				if (capacity_satisfied(json.options[i].car_type, passengers))
				{
					if (bestPrice.has(json.options[i].car_type))
					{
						if (json.options[i].price < bestPrice.get(json.options[i].car_type))
						{
							bestPrice.set(json.options[i].car_type, json.options[i].price);
							bestSupplier.set(json.options[i].car_type, 'Jeff\'s Taxis');
						}
					}
					else
					{
						bestPrice.set(json.options[i].car_type, json.options[i].price);
						bestSupplier.set(json.options[i].car_type, 'Jeff\'s Taxis');
					}
				}
			}
			callback();
		}
	})
}

app.get('/', function (request, response)
{
	response.setHeader('Cache-Control', 'no-cache');
	response.setHeader('Content-Type', 'application/json');
	var pickup = request.query.pickup;
	var dropoff = request.query.dropoff;
	var passengers = request.query.passengers;

	var result;
	if ((result = check_arguments(pickup, dropoff, passengers)) != true)
	{
		var jsonErrorResponse = {
    		"success": false,
    		"error": {
    			"status_code": 400,
    			"type_of_error": "Bad Request",
    			"error_message": result
    		}
		};
		response.status(400).send(JSON.stringify(jsonErrorResponse), null, 0)
	}
	else
	{	
		var bestPrice = new Dict();
		var bestSupplier = new Dict();

		callDave(pickup, dropoff, passengers, bestPrice, bestSupplier, function(){
			callEric(pickup, dropoff, passengers, bestPrice, bestSupplier, function(){
				callJeff(pickup, dropoff, passengers, bestPrice, bestSupplier, function(){

					//sort results
					var sortedBestPrice = [];
					var sortedBestCarType = [];
					var temp = bestPrice.length

					for (var i = 0; i < temp; i++)
					{
						var currentLargestKey = null;
						var currentLargestPrice = 0;
						for (var key in bestPrice.store)
						{
							if (bestPrice.get(key) > currentLargestPrice)
							{
								currentLargestPrice = bestPrice.get(key);
								currentLargestKey = key
							}
						}
						bestPrice.delete(currentLargestKey)
						sortedBestPrice.push(currentLargestPrice)
						sortedBestCarType.push(currentLargestKey)
					}

					var finalResult = [];

					for (var i = 0; i < sortedBestPrice.length; i++) {
    					finalResult.push({
       					car_type: sortedBestCarType[i],
        				supplier: bestSupplier.get(sortedBestCarType[i]),
        				price: sortedBestPrice[i]
    					});
					}

					if (finalResult.length != 0)
						response.status(200).send(JSON.stringify(finalResult), null, 0);
					else
					{
						var noCarResponse = {
    						"success": true,
    						"error": {
    							"status_code": 204,
    							"type_of_error": "No cars found",
    							"error_message": "Please try again later"
    							}
							};
						response.status(204).send(JSON.stringify(noCarResponse), null, 0)
					}
				})
			})
		});
	}
})

app.listen(port);

console.log('RESTful API server started on port: ' + port);
module.exports = {capacity_satisfied, check_arguments};