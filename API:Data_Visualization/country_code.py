# A separate module to hold the country code search function

from pygal.maps.world import COUNTRIES


def code_search(input):
    """A function to search through Pygal's country code file and return the code"""
    for code, name in COUNTRIES.items():
        if input == name:
            return code
    # Specific exceptions for countries with difficult names
    if input == 'Congo, Dem. Rep.':
        return 'cd'
    elif input == 'Libya':
        return 'ly'
    elif input == 'Congo, Rep.':
        return 'cg'
    elif input == 'Tanzania':
        return 'tz'
    elif input == 'Egypt, Arab Rep.':
        return 'eg'
    elif input == 'Iran, Islamic Rep.':
        return 'ir'
    elif input == 'Bolivia':
        return 'bo'
    elif input == 'Venezuela, RB':
        return 've'
    elif input == 'Yemen, Rep.':
        return 'ye'
    # Returning none if the country of interest was not found
    return None
