# Author : Matthew Palomar
# 8/13/15
# codeabbey.com Problem #7
# http://www.codeabbey.com/index/task_view/fahrenheit-celsius

# Desc: Given n temperatures in Fahrenheit, convert to Celsius
# Input: n integers (Fahrenheit Temps)
# Output: List of n integers (Celsius Temps)

"""
ftc(5)

Data:
5 Entries
Entry 1 of 5: 495
Entry 2 of 5: 353
Entry 3 of 5: 168
Entry 4 of 5: -39
Entry 5 of 5: 22

Answer:
257 178 76 -39 -6
"""

def ftc(length):
	total = length
	count = 1
	results = []
	
	print("\nData:\n%i Entries" % total)

	while length >= 1:
		data = raw_input("Entry %i of %i: " % (count, total))
		length -= 1
		count += 1
		convData = (int(data) - 32)/1.8

		results.append(int(round(convData)))

	print("\nAnswer: ")

	for x in results:
		print x,

	return None