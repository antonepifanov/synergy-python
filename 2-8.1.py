N = int(input("Введите количество чисел: "))
numbers = []

# Считываем N чисел
for i in range(N):
   num = int(input())
   numbers.append(num)

# Переворачиваем список
reversed_numbers = numbers[::-1]

# Выводим результат
for num in reversed_numbers:
   print(num)