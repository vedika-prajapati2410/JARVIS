import time
import weather
import webbrowser
import voice as v

# print("Hello How can i assist you today..")
# print("Would you want me to open:-  \n1.Youtube \n2.Google \n3.Time \n4.Weather :- ")
while True:
    a = v.wake("jarvis")

    if not a:
        continue

    userinput = a.upper()
    current_time = time.localtime()

    if userinput == "WHAT IS THE TIME":
        print(f"Time = {current_time.tm_hour} : {current_time.tm_min}  : {current_time.tm_sec} | Date = {current_time.tm_mday}/{current_time.tm_mon}/{current_time.tm_year}")
    elif userinput == "WHAT IS THE WEATHER":
        weather.weather_current()
    elif userinput == "OPEN YOUTUBE":
        webbrowser.open("www.youtube.com")
    elif userinput == "OPEN GOOGLE":
        webbrowser.open("www.google.com")
    else:
        url = "https://www.google.com/search?q=" + a.replace(" ", "+")
        webbrowser.open(url)

