from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying the {from_file} to {to_file}")

in_file = open(from_file) ; indata = in_file.read()

print(f"The input file is {len(from_file)} bytes long")

print(f"Does the outfile really exist? {exists(to_file)}")
print("Ready? Hit RETURN to continue, CNTRL_C to abort")
input('> ')

out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done!")

out_file.close()
in_file.close()

