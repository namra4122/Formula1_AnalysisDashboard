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

    return season_data


# Fetch race_data
def fetch_race_data(selected_value):
    race_api = f"https://ergast.com/api/f1/{selected_value}.json"
    race_data = []

    races = requests.get(race_api).json()["MRData"]["RaceTable"]["Races"]

    for race in races:
        race_data.append(race["raceName"])

    return race_data


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
        # html.Label("Dropdown 2"),
        dcc.Dropdown(
            id="race_dropdown", value=None, style={"height": "30px", "width": "250px"}
        ),
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


if __name__ == "__main__":
    app.run_server(debug=True)
