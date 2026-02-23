"""
program --> simulate dealing with atm passwd ??

"""
"""
login = False
for i in range(3):
    password = input("Please enter your password: ")
    if password == "abc":
        login = True
        print("--- logged in successfully ---")
        break
    if i in [0,1]:
        print("---- please try again ---")

if login == False:
    print("---- the account is locked ----")

"""

# for i in range(5):
#     print(i)
# else:
#     print("--- the loop completed ---")

# for i in range(5):
#     if i ==3:
#         break
#     print(i)
# else:
#     """ this block will be executed when the loop completed it work without break """
#     print("--- the loop completed ---")
#


# for i in range(5):
#     if i ==4:
#         continue # skip current iteration
#     print(i)
# else:
#     """ this block will be executed when the loop completed it work without break """
#     print("--- the loop completed ---")



""" """
for i in range(3):
    password = input("Please enter your password: ")
    if password == "abc":
        print("--- logged in successfully ---")
        break
    if i in [0,1]:
        print("---- please try again ---")
else:
    print("---- the account is locked ----")










