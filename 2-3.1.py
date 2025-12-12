# Запрашиваем данные у пользователя
pet_type = input("Введите вид питомца: ")
pet_age = input("Введите возраст питомца: ")
pet_name = input("Введите кличку питомца: ")

# Правильно склоняем слово "год"
age = int(pet_age)
if 11 <= age % 100 <= 19:
   age_word = "лет"
elif age % 10 == 1:
   age_word = "год"
elif 2 <= age % 10 <= 4:
   age_word = "года"
else:
   age_word = "лет"

result = f'Это {pet_type} по кличке "{pet_name}". Возраст: {pet_age} {age_word}.'
print(result)