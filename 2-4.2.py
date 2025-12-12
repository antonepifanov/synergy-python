number = int(input("Введите пятизначное число: "))

# Извлекаем цифры
units = number % 10                # единицы
tens = (number // 10) % 10         # десятки
hundreds = (number // 100) % 10    # сотни
thousands = (number // 1000) % 10  # тысячи
ten_thousands = (number // 10000) % 10  # десятки тысяч

# Вычисления
step1 = tens ** units
step2 = step1 * hundreds
result = step2 / (ten_thousands - thousands)

print("Результат:", result)