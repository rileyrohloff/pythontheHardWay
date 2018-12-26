# Some variable set up for the code format
types_of_people = 10
x = f"There are {types_of_people} types of people"


# More vairables for sentence structure
binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

#Printng the variable into strings
print(x)
print(y)

#formating them within an already existing string

print(f"I said: {x}")
print(f"I also said: '{y}''")

#varible with a "format" function in the joke evaluation expression

hilarious = False
joke_evaluation = "Isn't that joke so funny !? {}"

print(joke_evaluation.format(hilarious))

#piecing together a sentence with two variables into a string

w = "This is the left side of..."
e = "a string with a right side"

print(w + e)