
# defining a simple function to accept positional and keyword arguments


def make_shirt(size, text):
    """Takes the size of a shirt and the desired printed text"""
    print("\nSewing a " + size + " shirt with the following text:\n" + text.title() + ".")


make_shirt("small", "papa bob's")
make_shirt(size="small", text="papa bob's")

# defining a new test function


def city_country(city, country):
    """Takes the name and country of a city and returns a single string"""
    full_location = city + ", " + country
    return full_location.title()


while True:
    print("\n---Welcome to the city/country automater!---")
    print("Type 'q' at any time to exit")

    city = input("\nPlease type your city: ")
    if city.title() == 'Q':
        print("Exiting program...")
        break
    country = input("\nPlease type your country: ")
    if country.title() == 'Q':
        print("Exiting program...")
        break
    location = city_country(city, country)
    print("\nYour location is: " + location + ".")

# defining a new function to create a dictionary


def make_album(artist_name, album_title, year=" "):
    """Creates a dictionary from  artist name and album title with the optional year argument"""
    album = {'name': artist_name, 'title': album_title}
    if year:
        album['year'] = year
    return album


while True:
    print("\n---Welcome to the Python album compiler!---")
    print("Type 'q' at any time to exit")

    name = input("\nPlease type the album's artist: ")
    if name.title() == 'Q':
        print("Exiting program...")
        break
    title = input("\nPlease type your album's name: ")
    if title.title() == 'Q':
        print("Exiting program...")
        break
    y = input("\nDo you know the album's release year?: ")
    if y.title() == 'Y':
        year = input("\nPlease type the album's release year(Y/N): ")
    elif y.title() == 'Q':
        break
    else:
        year = " "
    album_info = make_album(name, title, year)
    print("\nYour album has the following information: ")
    print("Artist name: " + album_info['name'].title())
    print("Album title: " + album_info['title'].title())
    print("Year of publication : " + album_info['year'])

# creating a function to modify a list of magicians

print("\n---Welcome to the Mage Upgrader!---")


def great_magicians(mages, gmages):
    """A function to add 'great' to the beginning of each name"""
    while mages:
        holder = mages.pop()
        print(holder.title() + "'s power are increasing...")
        gmages.append("The Great " + holder)

# creating a function to print out a list


def show_mages(gmages):
    """Prints the names of the greater magicians"""
    print("\nCongratulations to these upgraded magicians: ")
    for name in gmages:
        print(name.title())


mages = ['peter', 'shaun', 'natalie', 'bella']
gmages = []
great_magicians(mages, gmages)
show_mages(gmages)

# creating a function to accept an arbritrary argument
print("\n---Welcome to the sandwich machine!---")
print("Watch as it assembles three different sandwiches")


def sandwich(bread, *ingredients):
    """Takes the requested type of bread and however many other ingreadients are requested"""
    print("\nMaking a sandwich on " + bread + " bread with the following ingredients:")
    for name in ingredients:
        print("- " + name)


sandwich("white", "ketchup", "mustard", "mayo")
sandwich("wheat", "tofu", "hummus", "spinach")
sandwich("cardboard", "glass", "sawdust")

# creating a function to take an arbitrary number of key-value pairs


def build_profile(first, last, **profile_info):
    """Always takes first and last name information followed by other info"""
    profile = {}
    profile['first_name'] = first.title()
    profile['last_name'] = last.title()
    for key, value in profile_info.items():
        profile[key.title()] = value.title()
    return profile


user_profile = build_profile('joe', 'pickert',
                             hometown='lawrence',
                             school='university of kansas',
                             job='mountain guide')

print(user_profile)
