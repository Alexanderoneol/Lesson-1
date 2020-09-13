n = input("Enter an integer: ")

while n < '0':
    print("If you entered a negative number value? repeat only the positive value!")
    n = input('Please enternumber greater than 0: ')

    print(f"{n} + {n +n} + {n + n + n} = {int(n) + int(n +n) + int(n + n + n)}")