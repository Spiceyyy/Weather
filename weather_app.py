import requests
from tkinter import *

API_KEY = "9ee04c244e86fd079a942b2074595a87"
BASE_URL ="https://api.openweathermap.org/data/2.5/weather"
AIR_CODE = "http://api.openweathermap.org/data/2.5/air_pollution"

root = Tk()
root.geometry("800x200")

def cityForecast():
    global latitude
    global longtitude
    request_url = f"{BASE_URL}?appid={API_KEY}&q={city.get()}"
    response = requests.get(request_url)
    if response.status_code == 200:
        data = response.json()
        weather = data['weather'][0]['description']
        temperature = round(data['main']['temp'] - 273.5, 2)
        wind = round(data['wind']['speed'])
        cloud = data['clouds']['all']
        longtitude = round(data['coord']['lon'])
        latitude = round(data['coord']['lat'])
        myLabel = Label(root, text="Weather: " + str(weather) + "\nTemperature: " + str(temperature) + " Celsius " + "\nWind Speed: " + str(wind) + "\nCloudiness: " + str(cloud) + "%" + "\nLongtitude: " + str(longtitude) + 
                    "\nLatitude: " + str(latitude)    )
        myLabel.grid(row=1, column=0, columnspan=2)
        coords = {"lon": longtitude, "lat": latitude}
        if (city == "montreal"):
            request = f"{AIR_CODE}?appid={API_KEY}&lat=46&lon=-74"
            response = requests.get(request)
            if response.status_code == 200:
                air = response.json()
                print(air)

    else:
        print("An error occured.")

cityButton = Button(root, text="Insert City Name: ", command= lambda:[cityForecast()])
cityButton.grid(row=1, column=1, columnspan=2)

city = Entry(root)
city.grid(row=0, column=0)



root.mainloop()
