import collections

pets = {}

# Функция для получения информации о питомце по ID
def get_pet(ID):
   if ID in pets:
      return pets[ID]
   else:
      return False

# Функция для правильного склонения слова "год"
def get_suffix(age):
   if 11 <= age % 100 <= 19:
      return "лет"
   elif age % 10 == 1:
      return "год"
   elif 2 <= age % 10 <= 4:
      return "года"
   else:
      return "лет"

# Функция для отображения всех питомцев
def pets_list():   
   if not pets:  # если словарь пустой
      print("В базе данных нет питомцев.")
      return
   
   for pet_id, pet_info in pets.items():
      print(f"\nID: {pet_id}")
      
      # Извлекаем имя питомца и его данные
      pet_name = list(pet_info.keys())[0]
      pet_data = pet_info[pet_name]
      
      # Получаем правильное окончание для возраста
      age_word = get_suffix(pet_data["Возраст питомца"])
      
      # Выводим информацию
      print(f"  Кличка: {pet_name}")
      print(f"  Вид: {pet_data['Вид питомца']}")
      print(f"  Возраст: {pet_data['Возраст питомца']} {age_word}")
      print(f"  Владелец: {pet_data['Имя владельца']}")

# Функция CREATE
def create():
   print("ДОБАВЛЕНИЕ НОВОГО ПИТОМЦА")
   
   # Используем collections.deque для получения последнего ID
   if pets:  # если словарь не пустой
      last = collections.deque(pets, maxlen=1)[0]
      new_id = last + 1
   else:  # если словарь пустой (первый питомец)
      new_id = 1
   
   # Вводим данные
   pet_name = input("Введите кличку питомца: ")
   pet_type = input("Введите вид питомца: ")
   
   # Ввод возраста с проверкой
   while True:
      age_input = input("Введите возраст питомца: ")
      if age_input.isdigit():
         pet_age = int(age_input)
         if pet_age > 0:  # возраст должен быть положительным
               break
         else:
               print("Ошибка! Возраст должен быть больше 0.")
      else:
         print("Ошибка! Возраст должен быть числом.")
   
   owner_name = input("Введите имя владельца: ")
   
   # Создаем запись
   pets[new_id] = {
      pet_name: {
         "Вид питомца": pet_type,
         "Возраст питомца": pet_age,
         "Имя владельца": owner_name
      }
   }
   
   print(f"Питомец '{pet_name}' успешно добавлен с ID: {new_id}")

# Функция READ
def read():
   print("ПРОСМОТР ИНФОРМАЦИИ О ПИТОМЦЕ")
   
   # Ввод ID
   try:
      pet_id = int(input("Введите ID питомца: "))
   except ValueError:
      print("Ошибка! ID должен быть числом.")
      return
   
   # Получаем информацию о питомце
   pet_info = get_pet(pet_id)
   
   if pet_info == False:
      print(f"Питомец с ID {pet_id} не найден.")
      return
   
   # Извлекаем данные и выводим информацию
   for pet_name, pet_data in pet_info.items():
      age_word = get_suffix(pet_data["Возраст питомца"])
      
      print(f'Это {pet_data["Вид питомца"]} по кличке "{pet_name}".')
      print(f'Возраст питомца: {pet_data["Возраст питомца"]} {age_word}.')
      print(f'Имя владельца: {pet_data["Имя владельца"]}')

# Функция UPDATE
def update():
   print("ОБНОВЛЕНИЕ ИНФОРМАЦИИ О ПИТОМЦЕ")
   
   # Ввод ID
   try:
      pet_id = int(input("Введите ID питомца: "))
   except ValueError:
      print("Ошибка! ID должен быть числом.")
      return
   
   # Проверяем, существует ли питомец
   if pet_id not in pets:
      print(f"Питомец с ID {pet_id} не найден.")
      return
    
   # Получаем текущие данные
   pet_info = pets[pet_id]
   pet_name = list(pet_info.keys())[0]
   pet_data = pet_info[pet_name]
   
   print(f"Текущая информация о питомце '{pet_name}':")
   print(f"Вид: {pet_data['Вид питомца']}")
   print(f"Возраст: {pet_data['Возраст питомца']}")
   print(f"Владелец: {pet_data['Имя владельца']}")
   
   print("Введите новые данные (оставьте пустым, чтобы сохранить текущее):")
   
   # Обновляем вид
   new_type = input(f"Вид питомца [{pet_data['Вид питомца']}]: ")
   if new_type:
      pet_data['Вид питомца'] = new_type
   
   # Обновляем возраст
   new_age = input(f"Возраст [{pet_data['Возраст питомца']}]: ")
   if new_age:
      if new_age.isdigit():
         pet_data['Возраст питомца'] = int(new_age)
      else:
         print("Ошибка! Возраст должен быть числом.")
   
   # Обновляем владельца
   new_owner = input(f"Владелец [{pet_data['Имя владельца']}]: ")
   if new_owner:
      pet_data['Имя владельца'] = new_owner
   
   print(f"Информация о питомце '{pet_name}' обновлена!")

# Функция DELETE
def delete():
   print("УДАЛЕНИЕ ПИТОМЦА")
   
   # Ввод ID
   try:
      pet_id = int(input("Введите ID питомца: "))
   except ValueError:
      print("Ошибка! ID должен быть числом.")
      return
   
   # Проверяем существование
   if pet_id not in pets:
      print(f"Питомец с ID {pet_id} не найден.")
      return
   
   # Получаем имя питомца для подтверждения
   pet_name = list(pets[pet_id].keys())[0]
   
   # Подтверждение удаления
   confirm = input(f"Вы уверены, что хотите удалить питомца '{pet_name}'? (да/нет): ")
   
   if confirm.lower() == 'да':
      del pets[pet_id]
      print(f"Питомец '{pet_name}' удален из базы данных.")
   else:
      print("Удаление отменено.")

# Главная программа
def main():
   print("БАЗА ДАННЫХ ВЕТЕРИНАРНОЙ КЛИНИКИ")
   
   command = ""
   
   while command != 'stop':
      print("ДОСТУПНЫЕ КОМАНДЫ:")
      print("  create  - добавить питомца")
      print("  read    - посмотреть информацию")
      print("  update  - обновить информацию")
      print("  delete  - удалить питомца")
      print("  list    - показать всех питомцев")
      print("  stop    - выйти")
      
      command = input("\nВведите команду: ").lower().strip()
      
      if command == 'create':
         create()
      elif command == 'read':
         read()
      elif command == 'update':
         update()
      elif command == 'delete':
         delete()
      elif command == 'list':
         pets_list()
      elif command == 'stop':
         print("Выход из программы. До свидания!")
      else:
         print(f"Неизвестная команда: '{command}'")


main()