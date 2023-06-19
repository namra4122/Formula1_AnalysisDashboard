import dash
import dash_core_components as dcc
import dash_html_components as html

app = dash.Dash()

circuit_lat = 46.9589  # Replace with actual latitude value for selected circuit
circuit_lon = 7.40194  # Replace with actual longitude value for selected circuit


osm_url = f"https://www.openstreetmap.org/export/embed.html?bbox={circuit_lon},{circuit_lat},{circuit_lon},{circuit_lat}&layer=mapnik"

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
        html.Iframe(src=osm_url, style={"height": "300px", "width": "100%"}),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
