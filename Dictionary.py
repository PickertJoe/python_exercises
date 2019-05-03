# creating a dictionary of personal information
stranger = {
    'first_name' : 'pablo',
    'last_name' : 'sandoval',
    'hometown' : 'syracuse',
    'sport' : 'baseball'
}
print("The stranger's first name is " + stranger['first_name'].title() +".")
print("His last name is " + stranger['last_name'].title() + ".")
print("He was born in " +stranger['hometown'].title() +" and likes to play "
    + stranger['sport'] +".")

# using a loop to print all key-value pairs
for key, value in stranger.items():
    print("\nKey: " + key)
    print("Value: "+ value.title())

# creating a dictionary of friends and their favorite languages
favorites = {
    'ben' : 'english',
    'yarden' : 'hebrew',
    'michael' : 'german',
    'joe' : 'spanish',
    'wesley' : 'mandarin'
}
# reporting each person's favorite language
print("\nSome of my friends' favorite languages: ")
for name, value in favorites.items():
    print(name.title() + "'s favorite languge is " + value.title() +".")

# reporting only the names in my dictionary
print("\nI chose to include the following people in my list: ")
for name in favorites.keys():
    print(name.title())

# reporting only the languages in my dictionary
print("\nThese were some of my friends' favorite languages: ")
for language in favorites.values():
    print(language.title())

# creating a list of rivers and a country that they abutt
rivers = {
    'rhine' : 'germany',
    'danube' : 'romania',
    'yellow' : 'china'
}

# printing each river and its associated country
print('\nThese are some well known rivers and the countries they run through:')
for key, value in rivers.items():
    print('The ' + key.title() + ' River runs through ' + value.title() +'.')

# printing respective lists of just the rivers and countries respectively
print('\nThe rivers included in this list were:')
for river in rivers.keys():
    print('The ' + river.title())
print('\nThe countries included in this list were: ')
for country in rivers.values():
    [print(country.title())]

# creating a dictionary with nested lists of favorite bikes
bikebrands = {
    'joe' : ['giant', 'specialized'],
    'topher' : ['trek', 'salsa'],
    'alec' : ['yeti', 'trek']
}

print("These are a few of my friends' favorite bike brands: ")
for name, bikes in bikebrands.items():
    print(name.title() + "'s favorite bike brands are: ")
    for bike in bikes:
        print("\t" + bike.title())

# creating nested dictionaries
senators = {
    'ceasar' : {
        'praenomen' : 'gaius',
        'gens' : 'julius',
        'cognomen' : 'caesar',
        'offices' : ['quaestor', 'aedile', 'praetor', 'consul', 'dictator']
    },
    'cicero' : {
        'praenomen' : 'marcus',
        'gens' : 'tullius',
        'cognomen' : 'cicero',
        'offices' : ['quaestor', 'aedile', 'praetor', 'consul']
    },
    'clodius' : {
        'praenomen' : 'publius',
        'gens' : 'clodius',
        'cognomen' : 'pulcher',
        'offices' : ['quaestor', 'aedile', 'tribune of the plebs']
    }
}
print("\nThese are a few of Rome's most famous Senators:")
for senator, info in senators.items():
    print("\nCommon name: " + senator.title())
    print("\tFull name: " + info['praenomen'].title() + " " + info['gens'].title() + " " +
            info['cognomen'].title())
    print("\tMagesterial offices held: ")
    for office in info['offices']:
        print("\t\t" + office.title())
