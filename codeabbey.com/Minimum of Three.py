# Author : Matthew Palomar
# 8/11/15
# codeabbey.com Problem #5
# http://www.codeabbey.com/index/task_view/min-of-three

# Desc: Of n triplets of integers, return the smallest of each triplet
# Input: n triplets of integers separated by a space
# Output: List of the smallest integer of n triplets separated by a space

"""
min(3)

Data:
3 Triplets
Triplet 1 of 3: 7 3 5
Triplet 2 of 3: 15 20 40
Triplet 3 of 3: 300 550 137

Answer:
3 15 137
"""

def min(length):
	total = length
	count = 1
	result = []
	
	print("\nData:\n%i Triplets" % total)

	while length >= 1:
		data = raw_input("Triplet %i of %i: " % (count, total))
		length -= 1
		count += 1
		ints = map(int, data.split(" "))
		if ints[0] <= ints[1] and ints[0] <= ints[2]:
			result.append(ints[0])
		elif ints[1] <= ints[2] and ints[1] <= ints[0]:
			result.append(ints[1])
		else:
			result.append(ints[2])

	print("\nAnswer: ")

	for x in result:
		print x,

	return None