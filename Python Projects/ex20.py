from sys import argv
#my two starting arguments
script, input_file = argv


#creating functions
def print_all(f):
    print(f.read())

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

#first variable

current_file = open(input_file)

print("First let's print the whole file:\n")

#using function and variable
print_all(current_file)


print("Now let's rewind, kind of like a tape.")

#using function with variable
rewind(current_file)

print("Let's print three lines:")

#creating new variables and passing them through each time they're redifined. 
current_line = 1
print_a_line(current_line, current_file)


#puts us on line "2" of the file
current_line += 1
print_a_line(current_line, current_file)


#Puts us on line "3" of the file


current_line += 1
print_a_line(current_line, current_file)