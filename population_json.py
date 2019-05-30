# A program to read and analyze the data in population_data.json

import json
from comma import comma
from country_code import code_search
from pygal.maps.world import World
from pygal.style import RotateStyle

# Importing the data in the json file into a list
filename = "chapter_16/population_data.json"
with open(filename) as f:
    population_data = json.load(f)

# Building a dictionary of the population data
cc_populations = {}
for country in population_data:
    if country['Year'] == '2010':
        country_name = country["Country Name"]
        population = int(float(country["Value"]))
        code = code_search(country_name)
        if code:
            cc_populations[code] = population

# Creating three separate categories for different population ranges
cc_pop1, cc_pop2, cc_pop3 = {}, {}, {}
for code, population in cc_populations.items():
    if population > 1000000000:
        cc_pop1[code] = population
    elif population > 10000000:
        cc_pop2[code] = population
    else:
        cc_pop3[code] = population


wm_style = RotateStyle('#336699')
wm = World(style=wm_style)
wm.title = "World Population in 2010, by Select Countries"
wm.add('1bn+', cc_pop1)
wm.add('10m - 1bn', cc_pop2)
wm.add('0-10m', cc_pop3)

wm.render_to_file('country_populations_category.svg')
