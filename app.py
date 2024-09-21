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

# print(multilinestring)

# n = 5
# print(dir(n))
string1 = "boyboyss1"

# print(string1[2])

course = 'Python for beginners'

# print(course[0: 5])

# we can use formatted strings to ours advantage

# name = 'mosh hamedani'
# message = f'hi my name is {name}'
# print(message)
#
# print(message.upper())
#
# contains = 'Python' in course
# print(contains)

# print(7 % 5)

variable = 10
variable += 10
# print(variable)

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

# if has_high_income and has_good_credit:
#     print("Eligible for loan")
# else:
#     print("Not eligible for a loan")

# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# for i in range(1, 5):
#     print(i)

numbers = [1, 2, 3, 4, 5, 6]
numbers_copy = numbers.copy()
numbers.append(6)
# numbers.clear()
# numbers_copy is the copied list which contains the elements in the original list
# Tuples are read only lists
coordinates = (1, 2, 3)
# print(coordinates)
# print(numbers_copy)
# print(numbers)
# x, y, z = coordinates
# print(x)

# we use dictionaries to store key/value pairs. let's say dictionaries are like maps in Elixir
customer = {
    "name": "John Smith",
    "age": 30,
    "is_verified": True

}

print("The customer is " + str(customer['age']) + " years of age")


def greet_user(first_name, last_name):
    print(f"Hi {first_name} {last_name}")


print(greet_user("John", "Smith"))
# try:
#     age = int(input("Age: "))
#     income = 20000
#     risk = income / age
#     print(age)
# except ValueError:
#     print("Not a valid number")
# except ZeroDivisionError:
#     print("Age cannot be 0")

# try:
#     age = int(input("Age: "))
#     income = 2000
#     print(age)
# except ValueError:
#     print("Not a valid number")
# except ZeroDivisionError:
#     print("Age cannot be Zero")

# print("Age cannot be Zero")
# print("I am a Beast")
#
# print("Siezi toa ganji dadi")
# print("Siezi toa ganji dadi")
print("I do not trust the Adani deal and I also unfortunately don't have a say in the matter")


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self):
        print(f'move to point ({self.x}, {self.y})')


class Person:
    def __init__(self, name):
        self.name = name

    def talk(self):
        print(f"{self.name} can talk incredibly fluently")


point2 = Point(0, 0)

person3 = Person('Dean Kinyua')

person3.talk()
