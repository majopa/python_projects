# Author : Matthew Palomar
# 8/28/15
# codeabbey.com Problem #13
# http://www.codeabbey.com/index/task_view/weighted-sum-of-digits

# Desc: Compute a weighted sum of digits
# Input: n integers
# Output: n weighted sums separated by spaces
#		  wsd(1776) = 1 * 1 + 7 * 2 + 7 * 3 + 6 * 4 = 60

"""
wsd(3)

Data:
3 Entries
Entry 1 of 3: 9
Entry 2 of 3: 15
Entry 3 of 3: 1776

Answer:
9 11 60
"""

def wsd(entryAmount):
	totalEntries = entryAmount
	currentIteration = 1
	results = []
	
	print("\nData:\n%i Entries" % totalEntries)

	while entryAmount >= 1:
		data = raw_input("Entry %i of %i: " % (currentIteration, totalEntries))
		entryAmount -= 1
		currentIteration += 1

		ints = map(int, data.split(" "))
		
		for i in ints:
			current_int_length = len(str(i))
			result = 0
			myStr = str(i)

			while current_int_length >= 1:
				myDigit = int(myStr[current_int_length - 1])

				result += (myDigit * current_int_length)
				current_int_length -=1

			results.append(result)
			

	print("\nAnswer: ")
	for x in results:
		print x,

	return None