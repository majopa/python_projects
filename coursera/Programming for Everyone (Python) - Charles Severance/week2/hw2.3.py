# Author : Matthew Palomar
# Class: Coursera - Programming for Everybody (Python)
# Date : 6/11/15

'''
Write a program to prompt the user for hours and rate per hour using raw_input to compute gross pay.
Use 35 hours and a rate of 2.75 per hour to test the program (the pay should be 96.25).
You should use raw_input to read a string and float() to convert the string to a number.
Do not worry about error checking or bad user data.
'''

# This first line is provided for you

hrs = raw_input("Enter Hours: ")
rate = raw_input("Enter Rate: ")
print float(hrs) * float(rate)

raw_input()