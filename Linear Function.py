# Author : Matthew Palomar
# 8/17/15

# Desc: Determine the slope and y-intercept of a Linear Function, given a pair of points
#		y = mx + b
# Input: n pairs of points corresponding to the Linear Function
#		(x1, y1), (x2, y2), ..., (xn, yn)
# Output: The slope and y-intercept for n Linear Functions

"""
lin(2)

Data:
2 Entries
Data 1 of 2: 0 0 1 1
Data 2 of 2: 1 0 0 1

Answer:
(1 0) (-1 1)
"""

def lin(length):
	total = length
	count = 1
	result = []

	print("\nData:\n%i Entries" % total)

	while length >= 1:
		nextSet = raw_input("Data %i of %i: " % (count, total))
		length -= 1
		count += 1
		data = map(int, nextSet.split(" "))

		a = int((data[3] - data[1])/(data[2] - data[0]))
		b = int((data[1] - (a * data[0])))
		result.append("(%i %i)" % (a, b))

	print("\nAnswer: ")
	for x in result:
		print x,

	return None