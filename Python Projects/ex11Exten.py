#Testing some input values on my own



print("What is your weight class?", end=' ')
weight_input = int(input())
print("How old are you?", end=' ')
age_input = input()
kg_convert = round(weight_input / 2.2046226)

print(f"To confirm, you're competation weight class is {kg_convert}kg and your age group is{age_input}?")

print("Please confirm with a Yes/No input value", end='')
yes_no = input()

print(f"Thank you for your submission! You've selected {yes_no}")
