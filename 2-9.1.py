N = int(input("Введите количество чисел: "))
numbers = list(map(int, input("Введите числа через пробел: ").split()))

# Проверяем, что введено ровно N чисел
if len(numbers) != N:
   print(f"Ошибка: нужно ввести {N} чисел, а введено {len(numbers)}")
   exit()

# Преобразуем в множество
unique_numbers = set(numbers)

# Выводим количество уникальных чисел
print(f"Количество различных чисел: {len(unique_numbers)}")