# Author : Matthew Palomar
# 8/27/15
# codeabbey.com Problem #12
# http://www.codeabbey.com/index/task_view/modulo-and-time-difference

# Desc: Compute the difference between two time values (d, h, m, s)
# Input: n pairs of time coordinates d1, h1, m1, s1, d2, h2, m2, s2
# Output: n sets of time coordiantes formatted in parentheses, separated by a space
#			(d, h, m, s)

"""
timeDiff(3)

Data:
3 Entries
Entry 1 of 3: 1 0 0 0 2 3 4 5
Entry 2 of 3: 5 3 23 22 24 4 20 45
Entry 3 of 3: 8 4 6 47 9 11 51 13

Answer:
(1 3 4 5) (19 0 57 23) (1 7 44 26)
"""

def timeDiff(entryAmount):
	totalEntries = entryAmount
	currentIteration = 1
	results = []
	
	print("\nData:\n%i Entries" % totalEntries)

	while entryAmount >= 1:
		data = raw_input("Entry %i of %i: " % (currentIteration, totalEntries))
		entryAmount -= 1
		currentIteration += 1

		d1, h1, m1, s1, d2, h2, m2, s2 = map(int, data.split(" "))

		first_entry_in_seconds = d1 * 864000 + h1 * 3600 + m1 * 60 + s1
		second_entry_in_seconds = d2 * 864000 + h2 * 3600 + m2 * 60 + s2

		difference = second_entry_in_seconds - first_entry_in_seconds

		"""
		d = difference // 864000
		h = (difference // 3600) % 24
		m = (difference // 60) % 60
		s = difference % 60
		"""

		d = difference // 864000
		h = (difference % 864000) // 3600 % 24
		m = ((difference % 864000) % 3600) // 60
		s = ((difference % 864000) % 3600) % 60

		results.append("(%i %i %i %i)" % (d, h, m, s))

	print("\nAnswer: ")
	for x in results:
		print x,

	return None