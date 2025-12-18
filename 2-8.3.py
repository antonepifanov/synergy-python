# Ввод данных
m = int(input("Максимальный вес лодки: "))
n = int(input("Количество рыбаков: "))

# Считываем веса рыбаков
weights = []
for i in range(n):
   weight = int(input(f"Вес рыбака {i+1}: "))
   weights.append(weight)

# Сортируем веса по возрастанию
weights.sort()

left = 0          # самый легкий рыбак
right = n - 1     # самый тяжелый рыбак
boats = 0         # счетчик лодок

# Пока есть рыбаки для переправки
while left <= right:
   # Если остался один рыбак
   if left == right:
      boats += 1
      break
    
   # Пробуем посадить самого легкого и самого тяжелого
   if weights[left] + weights[right] <= m:
      # Они могут плыть вместе
      left += 1
      right -= 1
   else:
      # Тяжелый должен плыть один
      right -= 1
    
   boats += 1

print(f"Минимальное количество лодок: {boats}")