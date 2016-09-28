"""
calculator.py

Using our arithmetic.py file from Exercise02, create the
calculator program yourself in this file.
"""

from arithmetic import *


# Your code goes here
while True:
	input_string = raw_input("<<< ")
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
	elif token[0] == '*':
		num1 = int(token[1]) 
		num2 = int(token[2])
		print multiply(num1, num2)
	elif token[0] == '/':
		num1 = int(token[1]) 
		num2 = int(token[2])
		print divide(num1, num2)
	elif token[0] == 'square':
		num1 = int(token[1]) 
		print square(num1)
	elif token[0] == 'cube':
		num1 = int(token[1]) 
		print cube(num1)
	elif token[0] == 'power':
		num1 = int(token[1]) 
		num2 = int(token[2])
		print power(num1, num2)
	elif token[0] == 'mod':
		num1 = int(token[1]) 
		num2 = int(token[2])
		print mod(num1, num2)
	else:
		print "We don't know what are you talking about, girl!!!!"
	