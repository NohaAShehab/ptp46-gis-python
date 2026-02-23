def ask_for_int(message = "please enter an integer "):
    try:
        num = int(input(message))
    except Exception as e:
        print(e)
        return None
    else:
        print(f"num = {num}")
        return num
    finally:
        """ execution of finally preceeds the return  """
        print("------ thank you for using our app ---------")
    print("************************************")

print(ask_for_int("please enter an integer "))


def new():
    print("test")
    return "safd"
    print("----")