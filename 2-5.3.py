X = int(input("Минимальная сумма инвестиций: "))
A = int(input("Сумма у Майкла: "))
B = int(input("Сумма у Ивана: "))

# Проверяем условия
can_mike = A >= X
can_ivan = B >= X
can_together = (A + B) >= X

# Определяем результат
if can_mike and can_ivan:
    print(2)
elif can_mike:
    print("Mike")
elif can_ivan:
    print("Ivan")
elif can_together:
    print(1)
else:
    print(0)