

def ask_for_integer( message = "Please enter an integer: " ):
    while True:
        num = input(message)
        if num.isdigit():
            return int(num)
        print("--- please try again ---")


def ask_for_string(message="Please enter a string: "):
    while True:
        strr  = input(message)
        if strr.isalpha():
            return strr
        print("--- please try again ---")
