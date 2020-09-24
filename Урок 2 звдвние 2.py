data_sheet = list(input("Enter the number arbitrary value - "))
for i in range(1, len(data_sheet), 2):
    data_sheet[i - 1], data_sheet[i] = data_sheet[i], data_sheet[i - 1]

print(data_sheet)
