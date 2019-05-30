# A program to read and analyze the data in population_data.json
# Added specific catches for countries that the code_search function could not locate

import json
from country_code import code_search
from pygal.maps.world import World
from pygal.style import RotateStyle

# Importing the data in the json file into a list
filename = "chapter_16/gdp_json.json"
with open(filename) as f:
    gdp_data = json.load(f)

# Building a dictionary of the population data
cc_gdps = {}
for country in gdp_data:
    if country['Year'] == 2010:
        country_name = country["Country Name"]
        gpd = int(country["Value"])
        code = code_search(country_name)
        if code:
            cc_gdps[code] = gpd

wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = "GDP by Country (2010)"
wm.add('Gross Domestic Product ($/Yr)', cc_gdps)
wm.render_to_file('country_gdp_full.svg')
