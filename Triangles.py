# Author : Matthew Palomar
# 8/17/15

# Desc: Given n triplets of integers that represent the lengths of triangle legs,
# determine if a triangle is possible
# Input: n triplets of integers
# Output: 1 (yes) or 0 (no)

"""
tri(2)

Data:
2 Entries
Data 1 of 2: 3 4 5
Data 2 of 2: 1 2 4

Answer:
1 0
"""

def tri(length):
	total = length
	count = 1
	result = []

	print("\nData:\n%i Entries" % total)

	while length >= 1:
		nextSet = raw_input("Data %i of %i: " % (count, total))
		length -= 1
		count += 1
		data = map(int, nextSet.split(" "))

		if data[0] + data[1] >= data[2]:
			if data[1] + data[2] >= data[0]:
				if data[0] + data[2] >= data[1]:
					result.append(1)
				else:
					result.append(0)
			else:
				result.append(0)
		else:
			result.append(0)

	print("\nAnswer: ")
	for x in result:
		print x,

	return None