# Author : Matthew Palomar
# Class: Coursera - Programming for Everybody (Python)

'''
9.4 Write a program to read through the mbox-short.txt and figure out who has the sent the greatest number of mail messages. 
The program looks for 'From ' lines and takes the second word of those lines as the person who sent the mail. 
The program creates a Python dictionary that maps the sender's mail address to a count of the number of times they appear in the file. 
After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''

fname = raw_input("Enter file name: ")
if len(fname) < 1: 
	fname = "mbox-short.txt"
fh = open(fname)
counts = {}

for line in fh:
    if not line.startswith("From "):
        continue
    if line.startswith("From "):
        buffer = line.split()
        for i in buffer[1:2]:
    		if i in counts:
    			counts[i] += 1
    		else:
    			counts[i] = 1

for word in sorted(counts, key=counts.get, reverse=True)[0:1]:
    print word, counts[word]

raw_input()