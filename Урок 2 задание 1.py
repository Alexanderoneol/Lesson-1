
data_sheet = [('Mary', 'Smith', 4.59, 2021), 1, 3.3, True, False, 'Column', [5, 6],
              (7, 8, 8.5), {9: 'nine', 10: 'ten'}, {11, 12}, frozenset(), range(13), (b'fourteen'), TypeError]
for i, item in enumerate(data_sheet, 1):
    print(f"{i}) {item} - {type(item)}")

