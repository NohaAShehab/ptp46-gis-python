
import  re
def ask_for_name(message='Please enter name: '):
    # recursion
    name = input(message)
    if name.isalpha():
        return name
    print("----- please enter valid name: -----")
    return ask_for_name()


def ask_for_email(message='Please enter email: '):
    email = input(message)
    pattern =  r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
    if re.fullmatch(pattern, email):
        return email
    print("----- please enter valid email: -----")
    return ask_for_email()
