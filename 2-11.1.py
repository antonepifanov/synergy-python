def factorial(n):
   result = 1
   for i in range(1, n + 1):
      result *= i
   return result

def factorial_list(start_num):
   # Находим факториал исходного числа
   first_factorial = factorial(start_num)
   
   # Создаем список для результатов
   result_list = []
   
   # Добавляем факториалы в убывающем порядке
   for i in range(first_factorial, 0, -1):
      result_list.append(factorial(i))
   
   return result_list

# Основная программа
num = int(input("Введите натуральное число: "))

# Создаем список факториалов
factorials = factorial_list(num)

# Выводим результат
print(factorials)