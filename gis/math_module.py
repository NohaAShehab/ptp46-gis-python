
def sum_nums(num1 :int, num2 :int):
    """
    this function will return the sum of num1 and num2
    :param num1: must be number
    :param num2: must be number
    :return: int or None
    """
    if isinstance(num1, int) and isinstance(num2, int):
        res = num1 + num2
        return res
    else:
        print("--- num1, num2 must be integers ---")
        return


if __name__ == "__main__":
    """ this lines of code will be executed when running this file
    not when we import it. """
    print("*********** welcome to math module ***********")
