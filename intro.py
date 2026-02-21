"""
    this file explores the basic syntax of python
    you will learn how to define a variable
    print variable etc.
    this is saved in __doc__
"""

""" this string could be considered as a comment """

name = 'ahmed'
nAme = 'Ali'
print(name)
print(nAme)

# This a comment
# each variable has datatype --> interpreter detect datatype in the runtime
num = 10

# if = 10 # SyntaxError: invalid syntax

# print = 10 #
#
# print("iti")
# str , int = 10

# name = 'noha' # IndentationError: unexpected indent
day = 'Saturday'
if day == 'Saturday':
    print("---Wish you a good week")
elif day == 'Thursday':
    print("---The weekend is near ")
else:
    print("------- Keep moving forward --------")

# if (day==''){} else if () {}, else{}


bio = ("My name is Noha"
       "I works at ITI ")
print(bio)

bio2 = '''My name is Noha
I works at ITI
I lives in Mansoura'''
print(bio2)