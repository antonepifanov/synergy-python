N = int(input("Введите N: "))

# Вводим числа в одну строку
numbers_input = input("Введите числа через пробел: ")

# Преобразуем в список чисел
arr = list(map(int, numbers_input.split()))

# Проверяем, что введено ровно N чисел
if len(arr) != N:
   print(f"Ошибка: нужно ввести ровно {N} чисел, а введено {len(arr)}")
   exit()

# Удаляем последний элемент и вставляем его в начало
last = arr.pop()
arr.insert(0, last)

# Выводим результат
print(*arr)