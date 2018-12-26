from sys import argv

script, user_name, user_age = argv
prompt = 'User Input>  '

print(f"Hi {user_name}, I'm the {script} script!")
print(f"I'd like to ask you a few questions :)")
print(f"Do you like me {user_name}?")
likes = input(prompt)

# Testing user_name and then the input
print(f"Where do you live {user_name}?")
lives = input(prompt)

print(f"You're {user_age}, right?")
my_age = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

# Printing all the strings and inputs togther in long "f" string
print(f"""
Alright, so you said '{likes}' about liking me. You live in '{lives}', but I'm not sure where that is!
You also have a {computer} computer! You're also {user_age}yrs old! Nice!""")