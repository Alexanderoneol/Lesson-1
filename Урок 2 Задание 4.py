listing = input("Введите несколько слов, используя пробелы междусловами: ").split()
for n, i in enumerate(listing, 1):
    print(n, i) if len(i) <= 10 else print(n, (i[: 10]))
