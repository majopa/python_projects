# Author : Matthew Palomar
# Class: Coursera - Programming for Everybody (Python)
# Date : 6/24/15

'''
Write code using find() and string slicing (see section 6.10) to extract the number at the end of the line below.
Convert the extracted value to a floating point number and print it out.
'''

text = "X-DSPAM-Confidence:    0.8475";
#print float(text.split()[1])
print float(text[text.find(":")+1:])

raw_input()