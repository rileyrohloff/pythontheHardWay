#creating a mapping of state to abbreveation 

states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
}

#creating a basic set of states and some cities in them
cities = {
    'CA': 'San Francisico',
    'MI': 'Detroit',
    'FL': 'Jacksonville',
}

#adding some more cities

cities['NY'] = 'New York'
cities['OR'] = 'Portland'

#printing out some cities

print('-' * 10)
print("NY state has: ", cities['NY'])
print("OR state has: ", cities['OR'])

#print some states 
print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Florida's abbreviation is: ", states["Florida"])

#do it by using the states then cities dict
print("Michigan has: ", cities[states['Michigan']])
print("Florida has: ", cities[states['Florida']])

#print every state abbreviation 
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in states
print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now do both
print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} state in abbreviated {abbrev}")
    print(f"and has the city {cities[abbrev]}")


#safely get an abbreviation by state that might not be there
print('-' * 10)
state = states.get('Texas')

if not state:
    print('Sorry no, Texas')

#get a state with a default value

city = cities.get('TX', 'Does not exist')
print(f"The city for the state 'TX' is: {city}")



