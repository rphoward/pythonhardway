from sys import argv
import os.path

print(argv)
path, script, from_file, to_file = argv

print("Copying from {} to {}".format(from_file, to_file))
print(script)
# We could do these two on one line too, how?

try:
    in_file = open(from_file)
except FileNotFoundError:
    print("Creating New File")
    in_file = open(from_file, 'w')

indata = in_file.read()

print(" The input files is {} bytes long.".format(len(indata)))

print("does the input file exist? {}".format(os.path.exists(to_file)))

try:
    out_file = open(to_file)
except FileNotFoundError:
    print('Creating new output file')
    out_file = open(to_file, 'w')
print('Alright, DONE!')

out_file.close()
in_file.close()


