from sys import argv

script, filename = argv

print(f"Do you want to open {filename} as a new file?")
print("If 'Yes', press RETRUN. If 'NO' press CNTRL-C")
input(">")

print("Creating new file...")
target = open(filename, 'w')

target.truncate()

print(f"What would you like to enter in {filename}?")

line1 = input(">")
line2 = input(">")
line3 = input(">")


target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print(f"You created {filename} with '{line1}','{line2}' and '{line3}' as inputs")
target.close()