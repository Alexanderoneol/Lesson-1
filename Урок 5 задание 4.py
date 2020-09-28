rus_dic = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("text_44.txt", "a", encoding='utf-8') as new_file:
    with open("text_4.txt", encoding='utf-8') as my_file:
        line = my_file.read().split("\n")
        for i in line:
            i = i.split(" - ")
            new_file.writelines(rus_dic[i[0]] + ' - ' + i[1] + "\n")