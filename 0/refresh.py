
# from enum import Enum

# name = 'ravi dhavlesha'
# fullname = name + ' ' + name
# age = 33

# # Print name and age
# print(name, age)  # ravi dhavlesha 33
# # RAV DHAVLESHA Ravi Dhavlesha 14
# print(name.upper(), name.title(),  len(name))

# # Print type and instance of name and age
# print(type(name), type(age))  # <class 'str'> <class 'int'>
# print(type(name) == str)  # True
# print(type(age) == str)  # False

# print(isinstance(name, str), isinstance(age, int))  # True True

# print(type(age) != float)  # True
# print(type(float(age)) == float)  # True

# # Conditional
# if type(name) == str:
#     print('Name is str type')  # Name is str type

# if type(age) == str:
#     print('Age is str type')
# else:
#     print('Age is not str type')  # Age is not str type

# if type(age) == str:
#     print('Age is str type')
# elif type(age) == int:
#     print('Age is int type')  # Age is int type


# def is_adult(age):
#     return True if age > 18 else False


# print('18', is_adult(18))  # 18 False
# print('21', is_adult(21))  # 21 True

# name = "ravi dhavlesha"
# print(name[1])  # r
# print(name[1:3])  # avi
# print(name[3:])  # i dhavlesha
# print(name[:3])  # rav

# done = True
# print(type(done))  # <class 'bool'>
# if done:
#     print('yes')  # Yes
# else:
#     print('no')

# # All numbers(including negatives) except 0 are True, 0 is False
# # Empty strings are False else True
# # List, Tuples, Set and Dictionary is False if empty


# class Status(Enum):
#     ACTIVE = 1
#     INACTIVE = 0


# print(Status.ACTIVE.value)
# print(Status(1), Status['INACTIVE'], Status['INACTIVE'].value)
# print(list(Status))
# print(len(Status))

# age = input('What is your age?')
# print('Youe age is ' + age)

# # List - Mutable/Can be modified []
# sampleList = ["Ahmedabad", 1, "Bangalore", 2, "Mumbai", 2]
# print("Ahmedabad" in sampleList)  # True
# print(sampleList[4])  # Mumbai
# sampleList[5] = 3
# sampleList.append("Delhi")
# sampleList.extend([4, "Pune", 5])
# sampleList += ["Indore", 6, 7]
# sampleList.remove(7)
# # ['Ahmedabad', 1, 'Bangalore', 2, 'Mumbai', 3, 'Delhi', 4, 'Pune', 5, 'Indore', 6]
# print(sampleList)
# print(sampleList.pop(), sampleList.pop(2))  # 6 Bangalore
# print(sampleList)
# sampleList.insert(2, "Bangalore")
# print(sampleList)
# print(sampleList.reverse())
# print(sampleList)

# # Tuples - Immutable/Can't be modified ()
# sampleTuples = ("Ahmedabad", 1, "Bangalore", 2, "Mumbai", 2)
# print(sampleTuples)

# # Dictionaries - Key/Value pairs {key: value}
# sampleDic = {"name": "Ravi", "age": 30}
# print(sampleDic["name"])  # Ravi
# print(sampleDic.get("name"))  # Ravi
# print(sampleDic.get("fullname"))  # None
# print(sampleDic.get("city", "Bangalore"))  # Bangalore
# print(sampleDic, sampleDic.keys(), sampleDic.values())
# print(list(sampleDic.keys()), list(sampleDic.values(), list(sampleDic.items())))
# print(sampleDic)

# # Sets - Unordered tuples and mutable, Unique {}
# sampleSet1 = {"Ravi", "Dhavlesha"}
# sampleSet2 = {"Ravi", "Pri"}
# print(sampleSet1 & sampleSet2)
# print(sampleSet1 | sampleSet2)
# print(sampleSet1 - sampleSet2)

# # Functions
# def say_hello():
#     print("Hello!")


# say_hello()


# def hello_name(name="Bro"):
#     print("Hello " + name + "!")


# hello_name()
# hello_name("Ravi")


# def change(value, dic):
#     value = 2
#     dic["name"] = "Dhavlesha"
#     return True


# value = 1
# dic = {"name": "Ravi"}
# print(value, dic)
# change(value, dic)
# print(value, dic)


# def hello_1(name):
#     if not name:
#         return False
#     return True


# print(hello_1(0))
# print(hello_1(None))
# print(hello_1("Ravi"))

# # Variables declared outside the function can be accessed inside
# #  he function, but declared inside the function can't be accessed outisde the function

# # Nested Functions
# def talk(phrase):
#     def say(word):
#         print(word)

#     words = phrase.split(" ")
#     for word in words:
#         say(word)


# talk("This is sample a function to test nested functions")


# def count():
#     count = 0

#     def increment():
#         nonlocal count  # Access non local variable
#         count = count + 1
#         print(count)

#     increment()


# count()

# # Closures - Returning a function from  anested function which has access to
# # functions variable even when the nested function is not active anymore


# def count():
#     count = 0

#     def increment():
#         nonlocal count  # Access non local variable
#         count = count + 1
#         return count

#     return increment


# increment = count()
# print(increment())
# print(increment())
# print(increment())

# # Objects - Everything in python are objects including primitives
# # Has values and methods
# age = 3
# print(age.real, age.imag, age.bit_count(), age.bit_length())

# # Loops
# # While Loop
# val = 1
# while val <= 5:
#     print(val)
#     val = val+1

# items = ["A", "B", "C", "D"]
# for item in items:
#     print(item)

# for item in range(5):
#     print(item)

# items = ["A", "B", "C", "D"]
# for index, item in enumerate(items):
#     print(index, item)

# # Classes
# class SuperPerson:
#     def hi(self):
#         print("Hi")


# class Person(SuperPerson):
#     def __init__(self, name) -> None:
#         self.name = name

#     def hello(self):
#         print("Hello!" + ' ' + self.name)


# ravi = Person("Ravi")
# ravi.hello()
# print(ravi.name)
# ravi.hi()

# Modules - Every python file is module
# import module1
# module1.func_1()

# from module1 import func_1
# func_1()

# from lib import module2
# module2.func_2()

# from lib.module2 import func_2
# func_2()

# import sys
# print(sys.argv)

# Lambda functions - anonymous functions
# multiply = lambda a, b: a*b
# double = lambda num: num * 2

# numbers = [1, 2, 3]


# def double(a):
#     return a * 2


# result = map(double, numbers)
# print(list(result))

# numbers = [1, 2, 3]

# result = map(lambda a: a * 2, numbers)
# print(list(result))

# from functools import reduce

# expenses = [('Dinner', 90), ("Car", 20)]
# sum = reduce(lambda a, b: a[1] + b[1], expenses)
# print(sum)

# Recursions
# def factorial(n):
#     if n == 1:
#         return 1
#     return n * factorial(n - 1)


# print(factorial(5))

# # Decorators - HOF
# def logtime(func):
#     def wrapper():
#         print("before")
#         val = func()
#         print("after")
#         return val
#     return wrapper


# @logtime
# def hello():
#     print("Hello")


# hello()

# # Docstrings
# def hello():
#     """Print hello"""
#     print("Hello")


# print(help(hello))

# Annotations
# def increment(n: int) -> int:
#     return n + 1


# count: int = 0
# print(increment(count))

# # Exceptions
# try:
#     # Some lines to test
#     print("Try")
#     result = 2 / 0
#     print(result)
# except ZeroDivisionError:
#     # Handle EOFError
#     print("ZeroDivisionError")
# except:
#     #
#     print("Except")
# else:
#     # No exceptions were raised
#     print("Else")
# finally:
#     # Always run after all
#     print("Finally")


# try:
#     raise Exception("An error")
# except Exception as error:
#     print('Error', error)

# filename = "test.txt"
# try:
#     file = open(filename, "r")
#     content = file.read()
#     print(content)
# finally:
#     file.close()
# with open(filename, "r") as file:
#     content = file.read()
#     print(content)


# Third party packages - pip
# pypi.org - pypi - Python Package Index
# pip install requests  # Install
# pip uninstall requests  # Uninstall
# pip install - U requests  # Update

# # List compression
# numbers = [1, 2, 3, 4, 5]
# numbers_sqaure = [n ** 2 for n in numbers]
# print(numbers_sqaure)
