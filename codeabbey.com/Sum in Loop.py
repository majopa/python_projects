# Author : Matthew Palomar
# 8/10/15
# codeabbey.com Problem #2
# http://www.codeabbey.com/index/task_view/sum-in-loop

# Desc: Sum a list of n integers
# Input: n integers
# Output: Summation of n integers

"""
sum(8)

Data:
8 Entries
Entry 1 of 8: 10
Entry 2 of 8: 20
Entry 3 of 8: 30
Entry 4 of 8: 40
Entry 5 of 8: 5
Entry 6 of 8: 6
Entry 7 of 8: 7
Entry 8 of 8: 8

Answer:
36
"""

def sum(entryAmount):
	totalEntries = entryAmount
	currentIteration = 1
	results = []
	result = 0

	print("\nData:\n%i Entries" % totalEntries)

	while entryAmount >= 1:
		data = map(int,raw_input("Entry %i of %i: " % (currentIteration, totalEntries)))
		entryAmount -= 1
		currentIteration += 1

		result += data[0]

	print("\nAnswer: ")
	print result

	return None