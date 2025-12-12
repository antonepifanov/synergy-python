word = input("Введите слово из маленьких латинских букв: ")

# Счетчики
vowel_count = 0  # общее количество гласных
consonant_count = 0  # количество согласных

# Счетчики для каждой гласной
a_count = 0
e_count = 0
i_count = 0
o_count = 0
u_count = 0

# Проходим по каждой букве в слове
for letter in word:
    # Проверяем, является ли буква гласной
    if letter in "aeiou":
        vowel_count += 1
        
        # Считаем каждую гласную отдельно
        if letter == "a":
            a_count += 1
        elif letter == "e":
            e_count += 1
        elif letter == "i":
            i_count += 1
        elif letter == "o":
            o_count += 1
        elif letter == "u":
            u_count += 1
    else:
        consonant_count += 1

# Выводим общие результаты
print("Количество гласных:", vowel_count)
print("Количество согласных:", consonant_count)
print()

# Выводим количество каждой гласной (или False, если их нет)
print("Количество каждой гласной:")
print("a:", a_count if a_count > 0 else False)
print("e:", e_count if e_count > 0 else False)
print("i:", i_count if i_count > 0 else False)
print("o:", o_count if o_count > 0 else False)
print("u:", u_count if u_count > 0 else False)