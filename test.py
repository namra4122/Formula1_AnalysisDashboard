import requests


def update_circuitImg(race_value):
    circuit_api = f"http://ergast.com/api/f1/circuits/{race_value}.json"
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

    osm_url = f"https://www.openstreetmap.org/export/embed.html?bbox={circuit_lon-0.01},{circuit_lat-0.01},{circuit_lon+0.01},{circuit_lat+0.01}&layer=mapnik"
    return osm_url


print(update_circuitImg("monza"))
