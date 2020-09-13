num_select = int(input("Произведите ввод целого положительного числаЖ "))
max_value = num_select % 10
num = num_select

while num > 0:
    digit = num % 10
    if digit > max_value:
        max_value = digit
        if max_value == 9:
            break

    num = num // 10

print(f"Максимальная цфра вчисле {num_select} hdyf {max_value}")