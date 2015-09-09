# Author : Matthew Palomar
# Date: 8/27/15

# Desc: Compute the nth term of the Fibonacci Sequence
# Input: n, the number of fibonacci numbers you want to view
# Output: Fibonacci numbers up to n

"""
fib(10)

0
1
1
2
3
5
8
13
21
34
"""

from operator import add

def fib(n):
	prec, current = 0, 1
	k = 1
	print prec
	while k < n - 1:
		print current
		prec, current = current, prec + current
		k = k + 1
	return current

