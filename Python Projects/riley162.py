from sys import argv

script, filename = argv

print(f"Hi! Are you wanting to read, {filename}?")
input("> ")
target = open(filename, 'r')
print(target.read(5))