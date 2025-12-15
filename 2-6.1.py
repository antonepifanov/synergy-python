# Вводим количество чисел
N = int(input(""))

# Счетчик нулей
zero_count = 0

print(f"Введите {N} чисел:")
for i in range(N):
   number = int(input())
   if number == 0:
      zero_count += 1
      
print(f"Количество нулей: {zero_count}")