# mockweather  
To use, requires python 3 with the pyyaml package installed.    
(pip install pyyaml)   

usage: weather_cli.py [-h] [-d DATE] [-r RANGE] [-c CITY]  
  
Mock weather report cli.  
  
options:  
  -h, --help  show this help message and exit  
  -d DATE, --date DATE  start date (ISO format, ex 2024-01-02), defaults to todays date.  
  -r RANGE, --range RANGE  Range of days to report. defaults to 1  
  -c CITY, --city CITY  City Name to report on. Defaults to all cities. Current Cities: Chicago,Austin,Houston,Dallas  
  
ex:    
python weather_cli.py -d 1972-08-18 -r 5 -c Dallas   
{"report": [{"city": "Dallas", "weather": [{"date": "08-18-72", "Temperature": 68, "Humidity": 62, "Windspeed": 3}, {"date": "08-19-72", "Temperature": 88, "Humidity": 53, "Windspeed": 0}, {"date": "08-20-72", "Temperature": 37, "Humidity": 68, "Windspeed": 0}, {"date": "08-21-72", "Temperature": 3, "Humidity": 63, "Windspeed": 16}, {"date": "08-22-72", "Temperature": 100, "Humidity": 68, "Windspeed": 2}]}]}
