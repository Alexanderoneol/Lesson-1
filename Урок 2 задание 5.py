my_list = [9, 8, 7, 6, 6, 6, 5, 4, 3, 2, 2, 2, 1]
new_number = int(input("Введите новый элемент для построения рейтинга при условии, что это натуральное число: "))
i = 0
for n in my_list:
    if new_number <= n:
        i += 1
my_list.insert(i, new_number)
print(my_list)
