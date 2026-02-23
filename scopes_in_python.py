# course_name = "Python"
#
# def say_hi():
#     print(course_name)
#
#
# def test():
#     usrname= "Ali"
#
# test()
# print(usrname)

################################################
""" 1- global variable """
course_name = 'introduction to python'
print(course_name)

""" 2- local variable: any variable defined inside the function """
def say_hello():
    username= input("Enter your name: ")  # local variable can be accessed inside the function
    print(username)

# say_hello()

""" 3- access global variable from function """

def print_course_name():
    print(f"course name is {course_name}")

print_course_name()


"""4- modify global variable from a function"""
course_name = 'introduction to python'

def modify_course_name():
    global course_name # please use the global one don't create new local variable
    course_name= input("Enter your course name: ")
    print(course_name)

# print(f"--- before calling funciton {course_name} ---")
# modify_course_name()
# print(f"after calling: {course_name}")


""" ------> scopes and functions inside a function  <------- """

" print local variable from inner function "
def outer_function():
    username = "iti" # local variable
    """ local variable --> can be accessed from anywhere inside inner function"""
    def inner_function():
        print(f"----- from inner function username= {username}")

    inner_function()

outer_function()


""" modify local variable from inner function """

def outer_function2():
    username = "iti"

    def inner_function():
        username = input("Enter your username: ") # new local variable ??
        print(f"----- from inner function username= {username}")

    inner_function()
    print(username)

# outer_function2()

""" ============================"""

def outer_function3():
    username = "iti"

    def inner_function():
        nonlocal username
        username = input("Enter your username: ")
        print(f"----- from inner function username= {username}")

    inner_function()
    print(username)


outer_function3()



















