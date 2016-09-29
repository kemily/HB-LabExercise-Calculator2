def add(num1, num2):
    return num1 + num2


def subtract(num1, num2):
    return num1 - num2


def multiply(num1, num2):
    return num1 * num2


def divide(num1, num2):
    # Need to turn at least argument to float for division to
    # not be integer division
    return float(num1) / float(num2) 


def square(num1):
    # Needs only one argument
    return num1 * num1


def cube(num1):
    # Needs only one argument
    return num1 * num1 * num1


def power(num1, num2):
    return num1 ** num2  # ** = exponent operator


def mod(num1, num2):
    return num1 % num2

#Trying functions for variable arguments below

# def new_add(*arg):
#     input_string = arg
#     tokens = input_string.split()
#     print tokens
#     numbers = range(1, (len(tokens)-1))
#     print numbers
#     summ = 0
#     for i in numbers:
#         summ = summ + i
#     return summ


# print new_add(1,2,3,4,5)

def new_add(*arg):
    summ = 0
    for i in arg:
        summ = summ + i
    return summ

print new_add(1,2,3,4,5)