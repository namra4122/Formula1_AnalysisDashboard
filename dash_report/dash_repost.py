import dash
from dash import html, dcc, dash_table, Input, Output, callback
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import requests


app = dash.Dash(__name__, external_stylesheets=[dbc.themes.MORPH])


# Fetch season_data
def fetch_season_data():
    season_api = "https://ergast.com/api/f1/seasons.json?limit=100"
    season_data = []

    seasons = requests.get(season_api).json()["MRData"]["SeasonTable"]["Seasons"]

    for season in seasons:
        season_data.append(int(season["season"]))

    season_data.sort(reverse=True)

    return season_data


# Fetch race_data
def fetch_race_data(selected_value):
    race_api = f"https://ergast.com/api/f1/{selected_value}.json"
    races = requests.get(race_api).json()["MRData"]["RaceTable"]["Races"]

    global race_data
    race_data = {}
    for race in races:
        race_data.update({race["raceName"]: race["Circuit"]["circuitId"]})

    return list(race_data.keys())


app.layout = html.Div(
    [
        html.H1("Formula 1 Dashboard"),
        html.H2("Select Season :"),
        dcc.Dropdown(
            id="season_dropdown",
            options=fetch_season_data(),
            value=None,
            style={"height": "30px", "width": "150px"},
        ),
        html.Br(),
        html.H2("Select Race Name :"),
        dcc.Dropdown(
            id="race_dropdown", value=None, style={"height": "30px", "width": "250px"}
        ),
        html.Br(),
        html.Iframe(id="circuit_map", style={"height": "300px", "width": "10%"}),
    ],
    style={"padding-left": "15px", "padding-top": "15px"},
)


@app.callback(Output("race_dropdown", "options"), Input("season_dropdown", "value"))
def update_race_value(season_value):
    if season_value is None:
        # If no value is selected in the season dropdown, show an empty second dropdown
        return []
    else:
        # Fetch the options for the race dropdown based on the selected value in the season dropdown
        race_value = fetch_race_data(season_value)
        return race_value


@app.callback(
    Output("circuit_map", "src"),
    Input("race_dropdown", "value"),
    prevent_initial_call=True,
)
def update_circuitImg(race_value):
    circuit_api = f"http://ergast.com/api/f1/circuits/{race_data[race_value]}.json"
    circuit = requests.get(circuit_api).json()["MRData"]["CircuitTable"]["Circuits"]

    name = circuit[0]["circuitId"]
    locality = circuit[0]["Location"]["locality"]
    country = circuit[0]["Location"]["country"]

    geocode_url = f"https://nominatim.openstreetmap.org/search?q={name}+{locality}+{country}&format=json"
    response_json = requests.get(geocode_url).json()
    if len(response_json) > 0:
        location_data = response_json[0]
        circuit_lat = float(location_data["lat"])
        circuit_lon = float(location_data["lon"])

    osm_url = f"https://www.openstreetmap.org/export/embed.html?bbox={circuit_lon-0.0075},{circuit_lat-0.0075},{circuit_lon+0.0075},{circuit_lat+0.0075 }&layer=mapnik"
    return osm_url


if __name__ == "__main__":
    app.run_server(debug=True)
