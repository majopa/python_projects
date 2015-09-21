# Author : Matthew Palomar
# Date : 6/17/15

# Desc: Compute the hourly pay with 1.5 pay considered over 40 hours
# Input: hours (h), rate (r)

def computepay(h,r):
	h = float(h)
	r = float(r)
	if h > 40:
		return (40*r) + ((h-40)*(r*1.5))
   	else:
   		return h * r

h = raw_input("Enter Hours: ")
r = raw_input("Enter Rate: ")

p = computepay(h,r)

print "Pay: " , p

raw_input()