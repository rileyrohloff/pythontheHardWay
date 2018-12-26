def add(a, b):
    print(f"Adding weights {a} + {b}.")
    return a + b

def kilogram_conversion(a):
    print(f"Your weight ({a}) in lbs. ")
    return round(a / 2.2046226, 3)

def multiply(a,b):
    return a * b

print(f"What is your weight in lbs?", end=' ')
input1 = int(input(">>  "))

Adding = add(25, 25)
KG_1 = kilogram_conversion(input1)

print(f"Your weight is {KG_1} kgs and your input is {Adding}lbs ")

KG_2 = multiply(Adding,input1)
KG_3 = kilogram_conversion(KG_2)

print(f"Your input: {input1} times your weights: {Adding} is {KG_2} lbs and {KG_3} kgs")

print("Does this look correct?")
input(">>  ")

print(f"Great, so {KG_3} is your total score! WOW!")







