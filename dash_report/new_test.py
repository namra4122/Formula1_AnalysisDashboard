import requests
import dash
from dash import dcc, html

app = dash.Dash()

circuit_name = ("Jeddah Corniche Circuit",)
locality_name = "Jeddah"  # Replace with actual locality name value for selected circuit
country_name = (
    "Saudi Arabia"  # Replace with actual country name value for selected circuit
)

geocode_url = f"https://nominatim.openstreetmap.org/search?q={circuit_name}+{locality_name}+{country_name}&format=json"

response_json = requests.get(geocode_url).json()
if len(response_json) > 0:
    location_data = response_json[0]
    circuit_lat = float(location_data["lat"])
    circuit_lon = float(location_data["lon"])

osm_url = f"https://www.openstreetmap.org/export/embed.html?bbox={circuit_lon-0.01},{circuit_lat-0.01},{circuit_lon+0.01},{circuit_lat+0.01}&layer=mapnik"

app.layout = html.Div(
    [
        dcc.Dropdown(
            id="year-dropdown",
            options=[
                {"label": "2019", "value": "2019"},
                {"label": "2020", "value": "2020"},
                {"label": "2021", "value": "2021"},
            ],
            value="2019",
        ),
        dcc.Dropdown(id="circuit-dropdown"),
        html.Br(),
        html.Iframe(src=osm_url, style={"height": "300px", "width": "10%"}),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
