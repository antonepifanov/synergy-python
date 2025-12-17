word = input("Введите строку: ")

# Сравниваем строку с её перевернутой версией
if word == word[::-1]:
   print("yes")
else:
   print("no")