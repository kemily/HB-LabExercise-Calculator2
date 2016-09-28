"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
	input_string = raw_input("<<<")
	token = input_string.split(" ")
	if token[0] == 'q':
		break
	elif token[0] == '+':
		num1 = int(token[1]) 
		num2 = int(token[2])
		print add(num1, num2)
	elif token[0] == '-':
		num1 = int(token[1]) 
		num2 = int(token[2])
		print subtract(num1, num2)
		