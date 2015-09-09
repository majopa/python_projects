# Author : Matthew Palomar
# 8/17/15
# codeabbey.com Problem #8
# http://www.codeabbey.com/index/task_view/arithmetic-progression

# Desc: Calculates the sum of first members of arithmetic sequence
#		A + (A + B) + (A + 2B) + (A + 3B) + ...
# Input: A, B, N. A = first value of sequence, B = step size, N = number of first values to calculate.
# Output: N results of the arithmetic sequences in a list separated by a space

"""
seq(2)

Data:
2 Entries
Data 1 of 2: 5 2 3
Data 2 of 2: 3 0 10

Answer:
21 30
"""

def seq(length):
	total = length
	count = 1
	results = []
	
	print("\nData:\n%i Entries" % total)

	while length >= 1:
		data = raw_input("Data %i of %i: " % (count, total))
		length -= 1
		count += 1
		data = map(int, data.split(" "))
		
		result = data[0]
		while data[2] > 1:
			result = result + data[0] + (data[2] - 1) * data[1]
			data[2] -= 1

		results.append(result)

	print("\nAnswer: ")
	for x in results:
		print x,

	return None