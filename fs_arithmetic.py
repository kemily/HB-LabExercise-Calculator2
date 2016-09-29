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

def new_subtract(*arg):
    subs = arg[0]
    for i in arg[1:]:
        subs = subs - i
    return subs

print new_subtract(20, 5, 6)

def new_mult(*arg):
    ans = 1
    for i in arg:
        ans = ans * i
    return ans

print new_mult(1,5,6)

def new_divide(*arg):
    quo = float(arg[0])
    for i in arg[1:]:
        quo = quo / i
    return quo

print new_divide(5,7,8,10)

def new_square(*arg):
    if len(arg) > 1:
        return 'Sorry, you cannot square more than one number'
    elif len(arg) == 1:
        return arg[0] * arg[0]

print new_square (2,4)
print new_square (3)

def new_cube(*arg):
    if len(arg) > 1:
        return 'Sorry, you cannot cube more than one number'
    elif len(arg) == 1:
        return arg[0] * arg[0] * arg[0]

print new_cube(1,4,6)
print new_cube(4)

def new_power(*arg):
    exp = arg[0]
    for i in arg[1:]:
        exp = exp ** i
    return exp

print new_power(2,2,5)


def new_mod(*arg):
    mod = arg[0]
    for i in arg[1:]:
        if mod % i == 0:
            print 'Sorry, there is no remainder for your entries' 
            break
        elif mod > 0:
            print "You are getting modulo between %s and %s" % (mod, i)
            mod = mod % i  
            print "The remainder is", mod  
    return 'Goodbye!'

print new_mod(120, 50, 8)
print new_mod(120, 60, 30)