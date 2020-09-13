good = []
specification = {'наименование': '', 'цена': '', 'количество': '', 'артикул': ''}
analytics = {'наименование': [], 'цена': [], 'количество': [], 'артикул': []}
num = 0
while True:
    if input('Для выхлда из программы нажмите "E", для продолжения "Enter": ').upper() == 'E':
        break
    num += 1
    for f in specification.keys():
        acquisition = input(f'Введите значение артикул "{f}": ')
        specification[f] = int(acquisition) if (f == 'цена' or f == 'количество') else acquisition
        analytics[f].append(specification[f])  # Добавляем свойство в аналитику
    good.append((num, specification))  # Добавляем свойства в список товаров
    print(f'\n Текущая аналитика по товарам: \n {"*" * 38}')
    for key, value in analytics.items():
       print(f'{key[:25]:>30}: {value}')
    print("*"*30)
