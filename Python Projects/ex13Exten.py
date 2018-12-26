from sys import argv
#Testing my own command line arguments and inputs for this script. 


script, your_name = argv
prompt = '> '


print(f"This {script} is the file for this test")
print(f"Does your file name match? Is {your_name} your name?")
yes_no = input(prompt)

print(f"You selected: {yes_no}.")

print("If you ran this script correctly, this is the last line. YAY! :)")