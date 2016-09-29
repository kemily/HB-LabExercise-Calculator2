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



def square(*arg):
    """This function check if an user inputs one argument, if so, it returns the
       value of the squared number, if not it will give a message
    """
    # Needs only one argument
    if len(arg) == 1:
        return arg[0] * arg[0]
    else:
        return "Input only one number, to get it squared!"

print square(2)
print square(1, 3, 5, 6)


def cube(*arg):
    """This function check if an user inputs one argument, if so, it returns the
       value of the cubed number, if not it will give a message
    """
    # Needs only one argument
    if len(arg) == 1:
        return arg[0] * arg[0] * arg[0]
    else:
        return "Input only one number, to get it squared!"

print cube(2)
print cube(1, 3, 5, 6)

# def power(num1, num2):
#     return num1 ** num2  # ** = exponent operator

def power(*arg):
    """this function returns resuilt of exponention of the first number by the rest of the numbers"""
    #first number will be the base for the exponention
    power_total = arg[0]
    #the rest of the numbers are the exponents of the number
    for i in arg[1:]:
        power_total = power_total ** i
    return power_total

print power(2, 2, 3, 4)


def mod(num1, num2):
    return num1 % num2
