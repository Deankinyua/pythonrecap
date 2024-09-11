variable1 = 89
name = input("What is your name? ")

print("Hello " + name)

birth_year = int(input("Birth year: "))
age = str(2024 - birth_year)
print("You are " + age + " years old")
# The input() function always returns data as a string. So, we’re converting the
# result into an integer by calling the built-in int() function.

multilinestring = """
One of the key features of Python is that everything is an object, and the type is just one attribute of an object. As an illustration, we can assign a single integer to a variable, and use the Python built-in function dir for
finding out the attributes of the object. If you execute the following twolines in an interactive interpreter, it should become clear that a Pythoninteger is much more complex than just a number. Please feel free toexperiment also with other types!

"""

print(multilinestring)
