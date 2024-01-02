"""
weather_cli.py
cli interface for weather.py
"""
import argparse
import weather
import datetime



mw = weather.MockWeather("weather.yml")
current_cities = ','.join([c.name for c in mw.list_cities()])

parser = argparse.ArgumentParser(description='Mock weather report cli.')
parser.add_argument("-d", "--date",
                    type=datetime.date.fromisoformat,
                    help="start date (ISO format, ex 2024-01-02), defaults to todays date.")

parser.add_argument("-r", "--range",
                    type=int, 
                    help="Range of days to report. Defaults to 1")

parser.add_argument("-c", "--city",
                    type=str, 
                    help="City Name to report on. Defaults to all cities. Current Cities: {}".format(current_cities))

args = parser.parse_args()

print(mw.generate_json_report(city_name=args.city or None,
                              startday=args.date or None,
                              numdays=args.range or 1))
