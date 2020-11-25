##
# lists.py

# Defining a list
shopping = []

# Defining a prepoulated list
shopping = ['Bananas', 'Bread', 'Gluten']
random_list = ['string', 7, 3.14, True]

# Accessing values inside a list using the index
shopping[0]
random_list[2]
#shopping[3]    // This causes and IndexError

# Modifying a value inside the list
shopping[2] = 'Soy Milk'
print(shopping)
#shopping[3] = 'Eggs'   // This causes an IndexError

# Adding new things to our list
shopping.append('Eggs')
print(shopping)


##
# dictionary_notes.py
# Class notes on accessing and traversing keys and values in a dictionary

capitals = {'New Zealand':'Wgtn', 'Australia':'Sydney', 'Germany':'Berlin'}

# Checking for a key
capital = 'New Zealand'
if capital in capitals:
    print(capitals[capital])

# Modifying a value in a dictionary
capitals['Australia'] = 'Canberra'

# Checking for a value
wrong_capital = 'Sydney'
if wrong_capital in capitals.values():
    print("Sydney is not a capital city!")

# Checking for a key using get
country = "Germany"
print(capitals.get(capital))

country = "Spain"  # doesn't exist
print(capitals.get(country, country + " is not yet in the dictionary!"))



# Traversing a Dictionary

# Method 1 - traversing a dictionary on the key
# Where country is the key
# and capital is the value
for country in capitals.keys():
    capital = capitals[country]
    print(country, "=", capital)

# Method 2 - traversing a dictionary by item
# Where shoe is the key
# and shoe_type is the value
for country, capital in capitals.items():
    print(country, '=', capital)


#A List of Lists
l = [[1,2],[3,4],[5,6]]
print(l[1][0])


#A List of Dictionaries


##
# nested_lists_in_dic.py
# Lists inside dictionaries

favourite_movies = {'John':['Horror','Comedy','Action'],
                    'Joe':['Documentary'],
                    'Jane':['Romance','RomComs']}

for code, movies in favourite_movies.items():
    if len(movies) < 2:
        print(code, "favourite movie is: ")
    else:
        print(code, "favourite movies are: ")
    for movie in movies:
        print(movie)

##
# Lists in a Dictiionary
fav_movies = {
    'joe':['titanic'],
    'jane':['avatar', 'django unchained']}
for name, movies in fav_movies.items():
    print(name + "'s fav movies are:")
    for movie in movies:
        print("\t"+movie)



## A list of Dictionaries

# Make an empty list for storing aliens
aliens = []

# Make 30 green aliens.
for alien in range(30):
    new_alien =  {'colour':'green','points':5, 'speed':'slow'}
    aliens.append(new_alien)

# Make first three aliens change to harder alien
for alien in aliens[:3]:
    if alien['colour'] == 'green':
        alien['colour'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show the first 5 aliens
for alien in aliens[:5]:
    print(alien)


## Dic in a Dic
users = {'bny':{'first':'bunna',
                'last':'ny',
                'email':'bunna.ny@onslow.school.nz'
                },
         'sfairhall':{'first':'shane',
                'last':'fairhall',
                'email':'shane.fairhall@onslow.school.nz'
                },
         }
for username, user_info in users.items():
    print("Username:", username,
          "First:", user_info['first'],
          "Last:", user_info['last'],
          "Email", user_info['email'])
