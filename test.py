import requests
import pandas as pd

# race_df = pd.DataFrame()


def fetch_race_data(selected_value):
    race_api = f"https://ergast.com/api/f1/{selected_value}.json"
    race_data = []
    races = requests.get(race_api).json()["MRData"]["RaceTable"]["Races"]

    for race in races:
        race_data.append(
            {"raceName": race["raceName"], "circuitID": race["Circuit"]["circuitId"]}
        )

    temp_df = pd.DataFrame(race_data)
    race_df = race_df.append(temp_df)

    return race_df


print(fetch_race_data(2023))
