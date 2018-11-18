var expect = require('chai').expect;

describe('functionTests', function()
{
	//import functions
	var capacity_satisfied = require('../server.js').capacity_satisfied;
	var check_arguments = require('../server.js').check_arguments;

	it ('test_minibus_capacity_satisfied_function', function capacitySatisfied(finish)
	{
		expect(capacity_satisfied('MINIBUS', 16)).to.equal(true);
		finish();
	});

	it ('test_minibus_capacity_not_satisfied_function', function capacitySatisfied(finish)
	{
		expect(capacity_satisfied('MINIBUS', 17)).to.equal(false);
		finish();
	});

	it ('test_luxury_people_carrier_capacity_satisfied_function', function capacitySatisfied(finish)
	{
		expect(capacity_satisfied('LUXURY_PEOPLE_CARRIER', 6)).to.equal(true);
		finish();
	});

	it ('test_luxury_people_carrier_capacity_not_satisfied_function', function capacitySatisfied(finish)
	{
		expect(capacity_satisfied('LUXURY_PEOPLE_CARRIER', 7)).to.equal(false);
		finish();
	});

	it ('test_standard_capacity_satisfied_function', function capacitySatisfied(finish)
	{
		expect(capacity_satisfied('STANDARD', 3)).to.equal(true);
		finish();
	});

	it ('test_standard_capacity_not_satisfied_function', function capacitySatisfied(finish)
	{
		expect(capacity_satisfied('STANDARD', 5)).to.equal(false);
		finish();
	});

	it ('test_working_arguments', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', '-50,50', 3)).to.equal(true);
		finish()
	});

	it ('test_missing_arguments_pickup', function checkArguments(finish)
	{
		expect(check_arguments(null, '-50,50', 3)).to.equal("3 Parameters required. pickup=lat,lon dropoff=lat,lon passengers=<1-16>");
		finish()
	});

	it ('test_missing_arguments_dropoff', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', null, 3)).to.equal("3 Parameters required. pickup=lat,lon dropoff=lat,lon passengers=<1-16>");
		finish()
	});

	it ('test_missing_arguments_passengers', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', '-50,50', null)).to.equal("3 Parameters required. pickup=lat,lon dropoff=lat,lon passengers=<1-16>");
		finish()
	});

	it ('test_incorrect_pickup_format', function checkArguments(finish)
	{
		expect(check_arguments('-503434350', '-50,50', 3)).to.equal("Pickup must be in format: lat,lon. for example 3.42,-50.65");
		finish()
	});

	it ('test_incorrect_dropoff_format', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', '-503434350', 3)).to.equal("Dropoff must be in format: lat,lon. for example 3.42,-50.65");
		finish()
	});

	it ('test_invalid_pickup_coordinates', function checkArguments(finish)
	{
		expect(check_arguments('hello,hi', '-50,50', 3)).to.equal("Pickup co-ordinates must be numbers");
		finish()
	});

	it ('test_invalid_dropoff_coordinates', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', 'hello,hi', 3)).to.equal("Dropoff co-ordinates must be numbers");
		finish()
	});

	it ('test_out_of_range_lat', function checkArguments(finish)
	{
		expect(check_arguments('-500,50', '-50,50', 3)).to.equal("Latitude values are out of range. Latitude should be between -90 and 90");
		finish()
	});

	it ('test_out_of_range_lon', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', '-50,500', 3)).to.equal("Longitude values are out of range. Longitude should be between -180 and 180");
		finish()
	});

	it ('test_passengers_not_a_number', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', '-50,50', 'hello')).to.equal("passengers parameter must be an integer");
		finish()
	});

	it ('test_passengers_out_of_bounds', function checkArguments(finish)
	{
		expect(check_arguments('-50,50', '-50,50', 20)).to.equal("number of passengers must be between 1 and 16");
		finish()
	});

});