# def add(num1, num2):
#     return num1 + num2


# def subtract(num1, num2):
#     return num1 - num2


# def multiply(num1, num2):
#     return num1 * num2


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




def new_add(*arg):
    """This function takes an unknown number of arguments and return sum of them"""
    summ = 0
    for i in arg:
        summ = summ + i
    return summ

print new_add(1, 2, 3, 4, 5)

def subtract(*arg):
    """This function subtracts from the first number the rest of the numbers in the given range"""
    #first element will be the initial value of substraction, since we substruct from it
    subtraction = arg[0]
    #choosing the range from the second element till the end
    #this is what we are going to gradually substruct from the first element
    for i in arg[1:]:
        subtraction -= i
    return subtraction

print subtract(20, 4, 6, 8)

def multiply(*arg):
    """This function multiplies all the given parameters, number of which is inknown"""
    mult = 1
    for i in arg:
        mult = mult * i
    return mult

print multiply(1, 2, 3, 4, 5)

def divide(*arg):
    """This function divides all the elements by the first element in the given range"""
    div = float(arg[0])
    for i in arg[1:]:
        div = div / i
    return div

print divide(120, 4, 5, 3)
