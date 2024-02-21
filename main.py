import requests
from twilio.rest import Client
import config

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = config.OWM_API_KEY
account_sid = 'ACf34e250a54d623259604134513d19ae1'
auth_token = config.TWILIO_AUTH_TOKEN

parameters = {
    "lat": 63.894,
    "lon": -41.935,
    "cnt": 4,
    "appid": api_key,
}

response = requests.get(url=OWM_Endpoint, params=parameters)
response.raise_for_status()
weather_data = response.json()

weather_id = [forcast["weather"][0]["id"] for forcast in weather_data["list"]]

will_rain = False
for w_id in weather_id:
    if w_id < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain today. Remember to bring an ☔",
            from_=config.TWILIO_PHONE_N,
            to=config.MY_PHONE_N
        )
    print(message.status)
