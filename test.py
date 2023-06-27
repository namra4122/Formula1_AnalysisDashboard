import requests


def fetch_race_data(selected_value):
    race_api = f"https://ergast.com/api/f1/{selected_value}.json"
    races = requests.get(race_api).json()["MRData"]["RaceTable"]["Races"]

    global race_data
    race_data = {}
    for race in races:
        race_data.update({race["raceName"]: race["round"]})

    return race_data


def update_circuitImg(season_value, race_value):
    circuit_api = (
        f"http://ergast.com/api/f1/{season_value}/{race_data[race_value]}/circuits.json"
    )
    circuit = requests.get(circuit_api).json()["MRData"]["CircuitTable"]["Circuits"]

    name = circuit[0]["circuitId"]
    locality = circuit[0]["Location"]["locality"]
    country = circuit[0]["Location"]["country"]

    print(name, locality, country)


print(fetch_race_data(2022))

update_circuitImg(2022, "Bahrain Grand Prix")
