import requests
from datetime import datetime

api_key = "2f14204802173d00209286cf322de9d7"
project_weather = open("weather_text.txt","w")
location = input("Enter the city name: ")

complete_api_link = "https://api.openweathermap.org/data/2.5/weather?q="+location+"&appid="+api_key
api_link = requests.get(complete_api_link)
api_data = api_link.json()

temp_city = ((api_data['main']['temp']) - 273.15)
weather_desc = api_data['weather'][0]['description']
hmdt = api_data['main']['humidity']
wind_spd = api_data['wind']['speed']
date_time = datetime.now().strftime("%d %b %Y | %I:%M:%S %p")

print ("-------------------------------------------------------------",file = project_weather)
print ("Weather Stats for - {}  || {}".format(location.upper(), date_time),file = project_weather)
print ("-------------------------------------------------------------",file = project_weather)

print ("Current temperature is: {:.2f} deg C".format(temp_city),file = project_weather)
print ("Current weather desc  :",weather_desc,file = project_weather)
print ("Current Humidity      :",hmdt, '%',file = project_weather)
print ("Current wind speed    :",wind_spd ,'kmph',file = project_weather)
print("Output stored. Please check the project_weather file for the output.")
project_weather.close()