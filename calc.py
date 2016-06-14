import os
from sys import argv

script, input_file, seek = argv

def print_all(f):
    print f.read()

def rewind(f, d):
    i = int(d)
    print(i)
    f.seek(i, 0)

def print_a_line(line_count, f):
    print line_count, f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
print os.environ
print os.environ['PROGRAMFILES']
print os.environ.has_key('WINDOWSSDKVERSION')

#print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file, seek)

print "Let's print three lines:"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)