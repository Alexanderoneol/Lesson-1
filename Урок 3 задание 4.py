def my_exp_func(x, y):
    try:
        result = x ** y
    except TypeError:
        return "Enter a float number and a negative power"
    return result


print(my_exp_func(6.3, - 2))
