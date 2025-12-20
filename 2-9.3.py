# Вводим последовательность чисел
numbers = list(map(int, input("Введите числа через пробел: ").split()))

# Множество для хранения уже встреченных чисел
set = set()

# Проверяем каждое число
for num in numbers:
   if num in set:
      print("YES")
   else:
      print("NO")
      set.add(num)