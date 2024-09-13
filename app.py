variable1 = 89
# name = input("What is your name? ")
#
# print("Hello " + name)
#
# birth_year = int(input("Birth year: "))
# age = str(2024 - birth_year)
# print("You are " + age + " years old")
# The input() function always returns data as a string. So, we’re converting the
# result into an integer by calling the built-in int() function.

multilinestring = """
One of the key features of Python is that everything is an object, and the type is just one attribute of an object. As an illustration, we can assign a single integer to a variable, and use the Python built-in function dir for
finding out the attributes of the object. If you execute the following twolines in an interactive interpreter, it should become clear that a Pythoninteger is much more complex than just a number. Please feel free toexperiment also with other types!

"""

print(multilinestring)

n = 5
print(dir(n))
string1 = "boyboyss1"

print(string1[2])

# fuck_you = kdkdkdkdkkdkdlslsldlslk;
# a;
# a;
# a;
# alk;
# alkkkkkkdddddfjf
course = 'Python for beginners'

print(course[0: 5])

# we can use formatted strings to ours advantage

name = 'mosh hamedani'
message = f'hi my name is {name}'
print(message)

print(message.upper())

contains = 'Python' in course
print(contains)

print(7 % 5)

variable = 10
variable += 10
print(variable)

is_hot = True
is_cold = False

if is_hot:
    print("hot day")
elif is_cold:
    print('cold day')
else:
    print("beautiful day")

has_high_income = True
has_good_credit = False

if has_high_income and has_good_credit:
    print("Eligible for loan")
else:
    print("Not eligible for a loan")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# for i in range(1, 5):
#     print(i)

numbers = [1, 2, 3, 4, 5, 6]
numbers.append(6)
numbers.clear()

# Tuples are read only lists
coordinates = (1, 2, 3)
print(coordinates)
print(numbers)
