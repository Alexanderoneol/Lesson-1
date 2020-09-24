def int_func():
    for word in input("Enter words with a space(lower latin script): \n").split():
        chars = 0
        for char in word:
            if 90 <= ord(char) <= 120:
               if chars == len(word):
                   print(word.title())
               else:
                   print(f"{word} - only small English letters!")
