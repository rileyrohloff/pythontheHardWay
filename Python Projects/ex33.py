i = 0
number = []
while i < 10:
    print(f"At the top i is {i}")
    number.append(i)
    i += 2

    print("number is now: ", number)
    print(f"At the bottom is {i}")

print("The numbers: ")

for num in number:
    print(num)

