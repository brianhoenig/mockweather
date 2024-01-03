import random
import yaml
import datetime
import json

class City():
    def __init__(self, city_data):
        """
        Build a mock city with dictionary of city data
        """
        self.name = city_data["name"]
        self.temp_range = (int(city_data["min-temp"]),
                           int(city_data["max-temp"]))
        self.humidity_range = (int(city_data["min-humidity"]),
                               int(city_data["max-humidity"]))
        self.windspeed_range = (int(city_data["min-windspeed"]),
                                int(city_data["max-windspeed"]))

    def get_random_temp(self):
        return random.randrange(self.temp_range[0],
                                self.temp_range[1])
                                
    def get_random_humidity(self):
        return random.randrange(self.humidity_range[0],
                                self.humidity_range[1])
        
    def get_random_windspeed(self):
        return random.randrange(self.windspeed_range[0],
                                self.windspeed_range[1])

class WeatherReport():
    def __init__(self, city, date):
        """ 
        given a city and a date, generate a random report.
        """
        self.city = city
        self.date = date

    def get_report(self):
        """
        generate a dict with random values for the weather points.
        """
        return {"date":self.date.strftime('%m-%d-%y'),
                "Temperature": self.city.get_random_temp(),
                "Humidity":self.city.get_random_humidity(),
                "Windspeed":self.city.get_random_windspeed()
                }
    
class MockWeather():

    def __init__(self, yaml_file):
        """
        init class with location of yaml file with city data
        """
        with open(yaml_file, 'r') as file:
            cities = yaml.safe_load(file)
        self.city_data = cities.get("Cities")
        
    def list_cities(self, city_name=None):
        """
        Return List(String) of all city names for this instance.
        Or a specific city if a name is specified.
        """
        if city_name:
            return [City(y) for y in self.city_data if y["name"] == city_name]
        else:
            return [City(y) for y in self.city_data]

        
    def generate_json_report(self, city_name=None, startday=None, numdays=1):
        """
        Generate a json report for one (or all cities)
        starting from startday (defaults to today)
        and for a givin range (defaults to 1)
        """
        if not startday:
            base = datetime.datetime.today()
        else:
            base = startday
            
        ret = {"report":[]}
        dates = [base + datetime.timedelta(days=x) for x in range(numdays)]
        
        for city in self.list_cities(city_name=city_name):
            city_report = {'city':city.name}
            weather_reports = []
            for date in dates:
                weather_reports.append(WeatherReport(city, date).get_report())
            city_report['weather'] = weather_reports
            ret["report"].append(city_report)

        return json.dumps(ret)
