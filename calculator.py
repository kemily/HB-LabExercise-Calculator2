"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
	input_string = raw_input("<<< ")
	token = input_string.split()
	num1 = int(token[1])
	if len(token) >= 3:
		num2 = int(token[2])
	
	if token[0] == 'q':
		break
	elif token[0] == '+':
		print add(num1, num2)
	elif token[0] == '-':
		print subtract(num1, num2)
	elif token[0] == '*':
		print multiply(num1, num2)
	elif token[0] == '/':
		print divide(num1, num2)
	elif token[0] == 'square':
		print square(num1)
	elif token[0] == 'cube':
		print cube(num1)
	elif token[0] == 'power':
		print power(num1, num2)
	elif token[0] == 'mod':
		print mod(num1, num2)
	else:
		print "We don't know what are you talking about, girl!!!!"
	