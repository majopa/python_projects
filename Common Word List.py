# Author : Matthew Palomar
# Class: 8/27/15

# Desc: Creates a list of commonly used words in a given file
# Input: file name (fname)

fname = raw_input("Enter file name: ")
fh = open(fname)
lst = list()
allWords = list()

for line in fh:
	linebuffer = line.rstrip().split()
	for words in linebuffer:
		allWords.append(words)

for words in allWords:
	if not words in lst:
		lst.append(words)

print sorted(lst)

raw_input()