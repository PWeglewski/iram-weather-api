import json
import urllib2

appid = '&APPID=9c709a0301484847a68727b947dec2b3'
location = 'Lodz,PL'


def cold_tommorow():
    max_allowed_temp_diff = 5;
    request = 'http://api.openweathermap.org/data/2.5/forecast/daily?q=' + location + appid + '&cnt=2'
    response = urllib2.urlopen(request)
    json_response = json.load(response);
    today_temp = json_response['list'][0]['temp']['day']
    tommorow_temp = json_response['list'][1]['temp']['day']
    temp_diff = float(today_temp) - float(tommorow_temp)
    if temp_diff < max_allowed_temp_diff:
        return False
    else:
        return True


def sunny_today():
    request = 'http://api.openweathermap.org/data/2.5/weather?q=' + location + appid
    response = urllib2.urlopen(request)

    # See http://openweathermap.org/weather-conditions
    sunny_weather_id = 800

    json_response = json.load(response);
    weather_id = json_response['weather'][0]['id']

    if weather_id == sunny_weather_id:
        return True
    else:
        return False


print('cold_tommorow(): ')
print(cold_tommorow())
print
print('sunny_today(): ')
print(sunny_today())
