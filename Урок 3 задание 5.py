def summarize():
    result = 0
    while True:
        print(f"Текущая сумма = {result}")
        input_sum = input("Введите в строку числа с пробелами для подсчета суммы (# - символ для завершения), #")
        for value in input_sum:
            if value == "#":
                print(f"Окончательная сумма = {result}")
                break
            try:
                result += float(value)
            except ValueError:
                print(f"Значение {value} не использовалось в расчетах - неверный тип")
        else:
            # Если символа завершения программы не было, то продолжаем ввод данных
            continue
        # В эту часть программы мы попадем, если встретим символ завершения программы
        break
        return f"Окончательная сумма = {result}"