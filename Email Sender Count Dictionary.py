# Author : Matthew Palomar
# Date: 8/27/15

# Desc: Scan text file for 'From: ' and creates a dictionary count for each unique sender
# Input: File name (fname)

fname = raw_input("Enter file name: ")
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