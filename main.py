import requests
from twilio.rest import Client
will_rain=False
api_key="e7251fa239814408efa5859851f1caab"
OWM_Endpoint="https:/  /api.openweathermap.org/data/2.5/forecast"
account_sid="AC39e56a042e0551ecaec14ff231dcbe4e"
auth_token="bff72761723b381eb2425d4b52eb69a1"
weather_params={
    "lat":40.9793,
    "lon":74.1165,
    "appid": api_key,
    "cnt":4,
}
response=requests.get(OWM_Endpoint,params=weather_params)
response.raise_for_status()

weather_data=response.json()
for  hour_data in weather_data["list"]:
    condition_code=hour_data["weather"][0]["id"]
    if int(condition_code)<700:
        will_rain=True
if will_rain==True:
    client = Client(account_sid, auth_token)

    message = client.messages \
        .create(
        body="It is going to rain pack an umbrella.",
        from_='+18557942439',
        to='+15512194056'
    )
    print(message.status)