def div(var_1, var_2):
    try:
      var_1, var_2 = int(var_1), int(var_2)
      div_num = var_1 / var_2
    except ValueError:
        return "Value Error"
    except ZeroDivisionError:
        return "Division by zero excluded!"
    return round(div_num, 4)


print(div(input("Enter first number - "), input("Enter second number - ")))
