import requests
import json

def load_forecast():
    url = 'http://worldweather.wmo.int/pl/json/2167_pl.xml'
    json_data = requests.get(url)
    if json_data.status_code != 200:
        print("Couldn't get data")
    return json_data.json()

def save_forecast(path, forecast):
    with open(path, 'w') as file:
        json.dump(forecast, file, indent=4)

if __name__ == "__main__":
    forecast = load_forecast()
    if forecast:
        data = forecast['city']['forecast']['forecastDay'][:3]
        for i in range(len(data)):
            data[i] = json.loads(f'''
            {{
                "data_prognozy": "{data[i]['forecastDate']}",
                "maks_temp": "{data[i]['maxTemp']}",
                "min_temp": "{data[i]['minTemp']}"
            }}
            ''')

            print(f"Dnia {data[i]['data_prognozy']} maksymalna tempretatura bedzie wynosic {data[i]['maks_temp']} a minimalna {data[i]['min_temp']}")

        save_forecast("forecast.json",data)
    else:
        print("Nie można pobrać danych")

