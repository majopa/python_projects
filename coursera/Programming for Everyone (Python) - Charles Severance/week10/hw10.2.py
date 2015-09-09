# Author : Matthew Palomar
# Class: Coursera - Programming for Everybody (Python)

'''
10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day for each of the messages. 
You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.

From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008

Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below. 
Note that the autograder does not have support for the sorted() function.
'''

fname = raw_input("Enter file name: ")
if len(fname) < 1: 
    fname = "mbox-short.txt"
fh = open(fname)
counts = {}
list = []

for line in fh:
    if not line.startswith("From "):
        continue
    
    if line.startswith("From "):
        buffer = line.split()
        for i in buffer[5:6]:
            list.append(i.split(":")[0])
               
for i in list:
    if i in counts:
        counts[i] += 1
    else:
        counts[i] = 1
        
for word in sorted(counts):
    print word, counts[word]

raw_input()