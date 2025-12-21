# Создаем пустой словарь
pets = {}

# Ввод данных
name = input("Кличка питомца: ")
animal = input("Вид питомца: ")
age = int(input("Возраст питомца: "))
owner = input("Имя владельца: ")

if 11 <= age % 100 <= 19:
   ending = "лет"
elif age % 10 == 1:
   ending = "год"
elif 2 <= age % 10 <= 4:
   ending = "года"
else:
   ending = "лет"

# Создаем словарь для одного питомца
pet_info = {}
pet_info['Вид питомца'] = animal
pet_info['Возраст питомца'] = age
pet_info['Имя владельца'] = owner

# Добавляем в основной словарь
pets[name] = pet_info
# Выводим результат
print(f'Это {list(pets[name].values())[0]} по кличке "{list(pets.keys())[0]}". {list(pets[name].keys())[1]}: {list(pets[name].values())[1]} {ending}. {list(pets[name].keys())[2]}: {list(pets[name].values())[2]}')