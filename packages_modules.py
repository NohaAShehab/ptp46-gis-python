

"1- import the module  ?"
# import inputs_module
#
# print(inputs_module.ask_for_integer("Please enter an integer"))

""" import part of the module """
# from inputs_module import ask_for_string
#
# print(ask_for_string("please enter firstname : "))

""" import from package """

# import gis.math_module
#
# res = gis.math_module.sum_nums(3,5)
# print(res)

""" alias module name """
# import gis.math_module as mth
#
# res = mth.sum_nums(3,5)
# print(res)


""" import part of the module (inside a package ?? )"""

# from gis.math_module import  sum_nums
# print(sum_nums(3,4))



""" --- check this scenario  ---"""
# import gis.math_module
# print(gis.math_module.sum_nums(3,4))


""" packages contains __init__ """
import iti
iti.say_hello("Ahmed")

iti.test()
iti.start()
