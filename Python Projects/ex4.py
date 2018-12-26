my_name = 'Riley Rohloff'
my_age = 22
my_height = 74 * round(2.54) #inches
my_weight = 210 # lbs
my_eyes = 'Blue'
my_teeth = 'White'
my_hair = 'Blonde'
cm = round(2.54)
kg = my_weight / 2.2046226
print(f"Let's talk about {my_name}.")
print(f"He's {my_height} inches tall")
print(f"He's {my_weight} pounds heavy")
print("Actually that's not too heavy")
print(f"He's got {my_eyes} eyes and {my_hair} hair")
print(f"His teeth are usually {my_teeth} depending on the coffee")

# this line is tricky
total = my_age + my_height + my_weight
print(f"If I add {my_age},{my_height}cm,and {round(kg, 3)}kg I get {total}")