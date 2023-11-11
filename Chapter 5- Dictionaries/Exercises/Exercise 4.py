#Rivers
#Dictionary of country and river that runs through them
rivers = {'nile':'egypt',
          'missouri':'united states',
          'yangtze':'china'}

#For loop to print the rivers and countries in sentences
for river, country in rivers.items():
    print('The '+river.capitalize()+' flows through '+country.capitalize()+'.')
print('\n')

#For loop to print the rivers
for river in rivers:
    print(river.capitalize())
print('\n')

#For loop to print the countries
for country in rivers.values():
    print(country.capitalize())