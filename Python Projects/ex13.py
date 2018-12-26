from sys import argv

#read the WYSS section of python documentation
script, first, second, third = argv

print("Your script is called: ", script)
print("Your first variable is: ", first)
print("Your third variable is:", second )
print("Your third variable is:", third)

print("What is your age?", end=' ')
your_age = int(input())
print("What is your weight?", end=' ')
your_weight = int(input())

print(f"Your age is {your_age} and your weight is {round(your_weight / 2.2046226)} in kgs.")