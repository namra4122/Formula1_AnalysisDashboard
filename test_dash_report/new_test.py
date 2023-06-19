# import dash
# import dash_core_components as dcc
# import dash_html_components as html
# from dash.dependencies import Input, Output
# import requests

# app = dash.Dash(__name__)


# # Fetch data for the first dropdown from the first API
# def fetch_dropdown1_data():
#     season_api = "https://ergast.com/api/f1/seasons.json?limit=100"
#     season_data = []

#     seasons = requests.get(season_api).json()["MRData"]["SeasonTable"]["Seasons"]

#     for season in seasons:
#         season_data.append(int(season["season"]))

#     return seasons


# # Fetch data for the second dropdown from the second API based on the selected value
# def fetch_dropdown2_data(selected_value):
#     race_api = f"https://ergast.com/api/f1/{selected_value}.json"
#     race_data = []

#     races = requests.get(race_api).json()["MRData"]["RaceTable"]["Races"]

#     for race in races:
#         race_data.append(race["raceName"])

#     return race_data


# app.layout = html.Div(
#     [
#         html.Label("Dropdown 1"),
#         dcc.Dropdown(id="dropdown-1", options=[], value=None),
#         html.Br(),
#         html.Label("Dropdown 2"),
#         dcc.Dropdown(id="dropdown-2", value=None),
#     ]
# )


# @app.callback(
#     Output("dropdown-1", "options"),
#     Output("dropdown-2", "options"),
#     Input("dropdown-1", "value"),
# )
# def update_dropdowns(dropdown1_value):
#     if dropdown1_value is None:
#         # If no value is selected in the first dropdown, show empty dropdowns
#         return [], []
#     else:
#         # Fetch the options for both dropdowns based on the selected value in the first dropdown
#         dropdown1_options = fetch_dropdown1_data()
#         dropdown2_options = fetch_dropdown2_data(dropdown1_value)

#         return dropdown1_options, dropdown2_options


# if __name__ == "__main__":
#     app.run_server(debug=True)


import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import requests

app = dash.Dash(__name__)


# Fetch data for the first dropdown from the first API
def fetch_dropdown1_data():
    season_api = "https://ergast.com/api/f1/seasons.json?limit=100"
    season_data = []

    seasons = requests.get(season_api).json()["MRData"]["SeasonTable"]["Seasons"]

    for season in seasons:
        season_data.append(int(season["season"]))

    return season_data


# Fetch data for the second dropdown from the second API based on the selected value
def fetch_dropdown2_data(selected_value):
    race_api = f"https://ergast.com/api/f1/{selected_value}.json"
    race_data = []

    races = requests.get(race_api).json()["MRData"]["RaceTable"]["Races"]

    for race in races:
        race_data.append(race["raceName"])

    return race_data


app.layout = html.Div(
    [
        html.Label("Dropdown 1"),
        dcc.Dropdown(id="dropdown-1", options=fetch_dropdown1_data(), value=None),
        html.Br(),
        html.Label("Dropdown 2"),
        dcc.Dropdown(id="dropdown-2", value=None),
    ]
)


@app.callback(Output("dropdown-2", "options"), Input("dropdown-1", "value"))
def update_dropdown2_options(dropdown1_value):
    if dropdown1_value is None:
        # If no value is selected in the first dropdown, show an empty second dropdown
        return []
    else:
        # Fetch the options for the second dropdown based on the selected value in the first dropdown
        dropdown2_options = fetch_dropdown2_data(dropdown1_value)
        return dropdown2_options


if __name__ == "__main__":
    app.run_server(debug=True)
