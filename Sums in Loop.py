# Author : Matthew Palomar
# 8/10/15

# Desc: Summation Loop for n pairs of integers
# Input: n pairs integers separated by a space
# Output: list of summations of n pairs of integers separated by a space

"""
sums(3)

Pair 1 of 3: 100 8
Pair 2 of 3: 15 245
Pair 3 of 3: 1945 54

Answer:
108 260 1999
"""

def sums(entryAmount):
	totalEntries = entryAmount
	currentIteration = 1
	result = []

	print("\nData:\n%i Entries" % totalEntries)

	while entryAmount >= 1:
		data = raw_input("Pair %i of %i: " % (currentIteration, totalEntries))
		entryAmount -= 1
		currentIteration += 1
		ints = map(int, data.split(" "))

		result.append(ints[0] + ints[1])

	print("\nAnswer: ")
	for x in result:
		print x,

	return None
