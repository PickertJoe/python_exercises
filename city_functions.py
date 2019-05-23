# This module contains a simple function to format a city's information


def city_country(city, country, population=""):
    """Takes a city's name, country, and population (optional) and returns it in neat format"""
    if population:
        city_formatted = city.title() + ", " + country.title() + "-- Population: " + population
    else:
        city_formatted = city.title() + ", " + country.title()
    return city_formatted
