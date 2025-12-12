number = int(input("Введите целое число: "))

# Проверяем, является ли число четным
is_even = (number % 2 == 0)

# Проверяем знак числа
if number > 0:
    sign = "положительное"
elif number < 0:
    sign = "отрицательное"
else:
    sign = "нулевое"

# Формируем описание
if number == 0:
    print("нулевое число")
elif is_even:
    print(f"{sign} четное число")
else:
    print(f"{sign} нечетное число")