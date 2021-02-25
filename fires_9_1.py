import json

in_file = open("US_fires_9_1.json", "r")
outfile = open("redable_US_Fires_9_1.json", "w")

fire_data = json.load(in_file)
json.dump(fire_data, outfile, indent=4)


lats, lons, brightness = ([] for i in range(3))

for fire in fire_data:
    if int(fire["brightness"]) > 450:
        lat = fire["latitude"]
        lon = fire["longitude"]
        bright = int(fire["brightness"])
        lats.append(lat)
        lons.append(lon)
        brightness.append(bright)

print(lats[:10])
print(lons[:10])
print(brightness[:10])
print(type(brightness[0]))

from plotly.graph_objs import Scattergeo, Layout
from plotly import offline

data = [
    {
        "type": "scattergeo",
        "lon": lons,
        "lat": lats,
        "marker": {
            # "size": [0.05 * bright for bright in brightness],
            "color": brightness,
            "colorscale": "Viridis",
            "reversescale": True,
            "colorbar": {"title": "Brightness"},
        },
    }
]


my_layout = Layout(title="California Fire")
fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="california_fire_9_1.html")
