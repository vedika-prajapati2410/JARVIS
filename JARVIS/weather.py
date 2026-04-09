import requests, json
def weather_current():
    api_key = "7040ea904442a45d6950ba584410ce59"
    base_url = "https://api.openweathermap.org/data/2.5/weather?q="
    city = input("Enter your city name: ")
    final_url = base_url + city + "&appid=" + api_key

    response = requests.get(final_url)

    data = response.json()

    print("Weather: ",data["weather"][0]["main"],",",data["weather"][0]["description"])    #[0] because weather is a list and we need to access the index first
    print("Current temperature: ",data["main"]["temp"]-273.15,"C")
    print("Current temperature feels like: ",data["main"]["feels_like"]-273.15,"C")
    print("Current humidity: ",data["main"]["humidity"])

