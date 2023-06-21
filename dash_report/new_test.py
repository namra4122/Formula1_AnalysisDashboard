import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import random

app = dash.Dash(__name__)

# Generate random map image and description
map_options = ["World", "USA", "Europe", "Asia", "Africa"]
map_choice = random.choice(map_options)
if map_choice == "World":
    img_url = "https://www.worldatlas.com/r/w1200-h630-c1200x630/upload/6a/8c/6d/world-map.jpg"
    description = "This is a map of the world."
elif map_choice == "USA":
    img_url = (
        "https://www.worldatlas.com/r/w1200-h630-c1200x630/upload/6a/8c/6d/usa-map.jpg"
    )
    description = "This is a map of the United States of America."
elif map_choice == "Europe":
    img_url = "https://www.worldatlas.com/r/w1200-h630-c1200x630/upload/6a/8c/6d/europe-map.jpg"
    description = "This is a map of Europe."
elif map_choice == "Asia":
    img_url = (
        "https://www.worldatlas.com/r/w1200-h630-c1200x630/upload/6a/8c/6d/asia-map.jpg"
    )
    description = "This is a map of Asia."
else:
    img_url = "https://www.worldatlas.com/r/w1200-h630-c1200x630/upload/6a/8c/6d/africa-map.jpg"
    description = "This is a map of Africa."

app.layout = html.Div(
    [
        html.Div(
            [html.Img(src=img_url)], style={"width": "50%", "display": "inline-block"}
        ),
        html.Div(
            [html.P(description)], style={"width": "50%", "display": "inline-block"}
        ),
    ]
)

if __name__ == "__main__":
    app.run_server(debug=True)
