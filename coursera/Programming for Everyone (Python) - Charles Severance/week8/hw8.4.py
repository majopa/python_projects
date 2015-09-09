# Author : Matthew Palomar
# Class: Coursera - Programming for Everybody (Python)

'''
8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the split() function.
The program should build a list of words. For each word on each line check to see if the word is already in the list and if not append it to the list. 
When the program completes, sort and print the resulting words in alphabetical order.
You can download the sample data at http://www.pythonlearn.com/code/romeo.txt
'''

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