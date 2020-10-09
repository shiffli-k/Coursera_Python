# Ordinance to find ASCII of character
print(ord('a'))
print(chr(42))

# python uses Unicode
my_list = [108, 105, 115, 116]
found_word = str()
for i in my_list:
    found_word += chr(i)
print(found_word)

