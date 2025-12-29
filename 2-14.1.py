my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16]

def print_list_recursive(lst, index=0):
   if index >= len(lst):
      print("Конец списка")
      return
   
   # Выводим текущий элемент
   print(lst[index])
   
   # Рекурсивный вызов для следующего элемента
   print_list_recursive(lst, index + 1)

print_list_recursive(my_list)