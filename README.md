# BookingGo Technical Test

## Dependencies
1. Python 3.6.4 (for part 1)  
URL: https://www.python.org/downloads/  
2. Node (for part 2)  
URL: https://nodejs.org/en/download/  
3. Copy repo by typing:  
`git clone https://github.com/arshia-mirabzadeh/BookingGoTechnicalTest.git`  
4. Download node dependencies by typing:  
`npm install` in main directory (containing package.json)  

## Part 1

### Print results of Dave's Taxis in descending price order

How to run:  
`python part1a.py pickup dropoff`

For example:  
`python part1a.py 54.237845,-21.153299 30.410632,-12.667513`

### With passenger number logic implemented

How to run:  
`python part1b.py pickup dropoff no_of_passengers`

For example:  
`python part1b.py 54.237845,-21.153299 30.410632,-12.667513 6`

### With extended search across all suppliers to find cheapest for each car type

How to run:  
`python part1c.py pickup dropoff`

For example:  
`python part1c.py 54.237845,-21.153299 30.410632,-12.667513 3`

## Part 2

### How to run the server

In the working directory, run:
`node server.js`

This should start the server. 

To send a request using the web, open any web browser and send a request using the url.

For example:  
`http://localhost:8080/?pickup=50,50&dropoff=50,50&passengers=3`

To send a request to the API using a terminal, run part2.py in a seperate shell after
running the server.

For example:  
`node server.js`  
`python part2.py 54.237845,-21.153299 30.410632,-12.667513 3`  

## Tests

Use the following command to run the tests for part1:  
`python tests.py`

Use the following command (in the main directory, not in test folder) to run the tests for part2:  
`npm test`

All the tests should pass
