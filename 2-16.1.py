class CashRegister:    
   def __init__(self, initial_amount):
      self.money = initial_amount
    
   def top_up(self, amount):        
      self.money += amount
      print(f"Касса пополнена на {amount} руб. Текущая сумма: {self.money} руб.")
    
   def count_1000(self):
      thousands = self.money // 1000
      print(f"В кассе {thousands} целых тысяч рублей.")
      return thousands
    
   def take_away(self, amount):        
      if amount > self.money:
         raise ValueError(f"Недостаточно денег в кассе! Запрошено: {amount} руб., доступно: {self.money} руб.")
        
      self.money -= amount
      print(f"Из кассы изъято {amount} руб. Остаток: {self.money} руб.")
    
# Создаем кассу с начальной суммой 5000 руб.
kassa = CashRegister(int(input("Введите начальное количество денег в кассе ")))
    
# Пополняем кассу
print("Пополнение кассы:")
kassa.top_up(int(input("Введите количество денег для пополнения ")))
    
# Считаем тысячи
print("\n2. Подсчет тысяч:")
kassa.count_1000()
    
# Изымаем деньги
print("\n3. Изъятие денег:")
try:
   kassa.take_away(int(input("Введите количество денег для изъятия ")))
except ValueError as e:
   print(f"Произошла ошибка: {e}")