def my_f(var_1, var_2):
    sub = var_1 / var_2
    print(f"sub: {sub}")


def my_f():
    var_1 = int(input("Введите значение 'var_1': "))
    var_2 = int(input("Введите значение 'var_2': "))
    sub = var_1 / var_2
    print(f"sub: {sub}")


def my_f(var_1: int = 44, var_2: int = 22):
    sub = var_1 / var_2
    print(f"sub: {sub}")
