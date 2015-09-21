# Author : Matthew Palomar
# 8/17/15

# Desc: Given triplets of integers, performs a calculation a returns a list of the results
# Input: n triplets of integers
# Output: List of n results

"""
sod(3)

Data:
3 Entries
Entry 1 of 3: 11 9 1
Entry 2 of 3: 14 90 232
Entry 3 of 3: 111 15 111

Answer:
1 16 21
"""

def sod(entryAmount):
	totalEntries = entryAmount
	currentIteration = 1
	results = []

	print("\nData:\n%i Entries" % totalEntries)

	while entryAmount >= 1:
		data = raw_input("Entry %i of %i: " % (currentIteration, totalEntries))
		entryAmount -= 1
		currentIteration += 1

		a, b, c = map(int, data.split(" "))
		result = (a * b + c)
		result = [int(i) for i in str(result)]
		iterations = len(result)
		finalResult = 0

		while iterations >= 1:
			finalResult = finalResult + result[(iterations-1)]
			iterations -= 1

		results.append(finalResult)

	print("\nAnswer: ")
	for x in results:
		print x,

	return None