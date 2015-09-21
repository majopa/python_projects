# Author : Matthew Palomar
# 8/13/15

# Desc: Given n pairs of integers, divide each pair and round up at 0.5 and greater
# Input: n pairs of integers
# Output: List of n quotients

"""
div(3)

Data:
3 Pairs
Pair 1 of 3: 12 8
Pair 2 of 3: 11 -3
Pair 3 of 3: 400 5

Answer:
2 -4 80
"""

def div(length):
	total = length
	count = 1
	result = []

	print("\nData:\n%i Pairs" % total)

	while length >= 1:
		data = raw_input("Pair %i of %i: " % (count, total))
		length -= 1
		count += 1
		ints = map(int, data.split(" "))
		result.append(int(round(round(ints[0])/ints[1])))

	print("\nAnswer: ")

	for x in result:
		print x,

	return None