# Author : Matthew Palomar
# Date: 8/27/15

# Desc: Prompts user for file name and then displays that file, line by line, in uppercase
# Input: file name (fname)

fname = raw_input("Enter file name: ")
fh = open(fname)

for line in fh:
    print line.upper().strip()

raw_input()