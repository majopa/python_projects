# Author : Matthew Palomar
# 8/11/15
# codeabbey.com Problem #4
# http://www.codeabbey.com/index/task_view/min-of-two

# Desc: Of n pairs of integers, return the smallest of each pair
# Input: n pairs of integers separated by a space
# Output: List of the smallest integer of n pairs

"""
min(3)

Data:
3 Pairs
Pair 1 of 3: 5 3
Pair 2 of 3: 2 8
Pair 3 of 3: 100 15

Answer:
3 2 15
"""

def min(length):
	total = length
	count = 1
	result = []
	
	print("\nData:\n%i Pairs" % total)

	while length >= 1:
		data = raw_input("Pair %i of %i: " % (count, total))
		length -= 1
		count += 1
		ints = map(int, data.split(" "))
		if ints[0] >= ints[1]:
			result.append(ints[1])
		else:
			result.append(ints[0])

	print("\nAnswer: ")

	for x in result:
		print x,

	return None