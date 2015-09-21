# Author : Matthew Palomar
# Date : 6/24/15

# Desc: Take in integer input until 'done' is entered and return largest and smallest.
# Input: n integers

largest = None
smallest = None

while True:
    num = raw_input("Enter an integer: ")

    if num == "done":
    	break

    try:
    	num = int(num)

    except ValueError:
    	print "Invalid input"
    	continue

    if smallest is None or num < smallest:
    	smallest = num
    if largest is None or num > largest:
    	largest = num

print "Maximum is", largest
print "Minimum is", smallest

raw_input()