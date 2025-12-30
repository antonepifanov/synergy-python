import os
import sys
import time
import random
import json
from datetime import datetime

# Константы для символов отображения
EMPTY = '·'
TREE = '🌲'
BURNING_TREE = '🔥'
BURNED_TREE = '🪵'
WATER = '🌊'
HELICOPTER = '🚁'
HOSPITAL = '🏥'
SHOP = '🛒'
CLOUD = '☁️'
LIGHTNING = '⚡'

class Game:
   def __init__(self, width=20, height=10):
      self.width = width
      self.height = height
      self.field = [[EMPTY for _ in range(width)] for _ in range(height)]
      self.helicopter = Helicopter()
      self.score = 0
      self.lives = 3
      self.water_capacity = 3
      self.water_level = 0
      self.tick = 0
      self.burning_trees = []
      self.clouds = []
      self.weather = 'sunny'  # sunny, rainy, stormy
      self.weather_duration = 0
      self.game_over = False
      self.game_won = False
        
   def generate_rivers(self):
      """Генерация рек на карте"""
      num_rivers = random.randint(2, 4)
      for _ in range(num_rivers):
         # Выбираем случайную точку на краю карты
         if random.choice([True, False]):
            # Горизонтальная река
            y = random.randint(0, self.height - 1)
            length = random.randint(5, self.width // 2)
            x_start = random.randint(0, self.width - length)
            for x in range(x_start, min(x_start + length, self.width)):
               self.field[y][x] = WATER
         else:
            # Вертикальная река
            x = random.randint(0, self.width - 1)
            length = random.randint(3, self.height // 2)
            y_start = random.randint(0, self.height - length)
            for y in range(y_start, min(y_start + length, self.height)):
               self.field[y][x] = WATER
    
   def generate_trees(self):
      """Генерация деревьев на карте"""
      num_trees = random.randint(self.width * self.height // 5, self.width * self.height // 3)
      for _ in range(num_trees):
         while True:
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            if self.field[y][x] == EMPTY:
               self.field[y][x] = TREE
               break
   
   def generate_hospital(self):
      """Генерация госпиталя"""
      while True:
         x = random.randint(0, self.width - 1)
         y = random.randint(0, self.height - 1)
         if self.field[y][x] == EMPTY:
            self.field[y][x] = HOSPITAL
            self.hospital_pos = (x, y)
            break
   
   def generate_shop(self):
      """Генерация магазина улучшений"""
      while True:
         x = random.randint(0, self.width - 1)
         y = random.randint(0, self.height - 1)
         if self.field[y][x] == EMPTY:
            self.field[y][x] = SHOP
            self.shop_pos = (x, y)
            break
   
   def generate_clouds(self):
      """Генерация облаков"""
      if self.weather != 'sunny':
         num_clouds = random.randint(1, 3)
         for _ in range(num_clouds):
            x = random.randint(0, self.width - 1)
            y = random.randint(0, self.height - 1)
            self.clouds.append({'x': x, 'y': y, 'type': CLOUD})
            
            if self.weather == 'stormy':
               # Добавляем молнии к некоторым облакам
               if random.random() < 0.3:
                  self.clouds[-1]['type'] = LIGHTNING
                  # Молния может поджечь дерево
                  if self.field[y][x] == TREE:
                     self.field[y][x] = BURNING_TREE
                     self.burning_trees.append({'x': x, 'y': y, 'burn_time': 5})
   
   def start_fire(self):
      """Начало пожара в случайном месте"""
      if random.random() < 0.1:  # 10% шанс на каждом тике
         burning_trees = [(tree['x'], tree['y']) for tree in self.burning_trees]
         available_trees = []
         
         # Ищем деревья, которые еще не горят
         for y in range(self.height):
            for x in range(self.width):
               if self.field[y][x] == TREE and (x, y) not in burning_trees:
                  available_trees.append((x, y))
         
         if available_trees:
            x, y = random.choice(available_trees)
            self.field[y][x] = BURNING_TREE
            self.burning_trees.append({'x': x, 'y': y, 'burn_time': 5})
            print(f"🔥 Начался пожар в ({x}, {y})!")
   
   def update_fires(self):
      """Обновление состояния пожаров"""
      new_burning_trees = []
      
      for fire in self.burning_trees:
         x, y = fire['x'], fire['y']
         fire['burn_time'] -= 1
         
         if fire['burn_time'] <= 0:
            # Дерево сгорело
            self.field[y][x] = BURNED_TREE
            self.score -= 10
            print(f"💔 Дерево в ({x}, {y}) сгорело! -10 очков")
            
            # Пожар может распространиться на соседние деревья
            for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
               nx, ny = x + dx, y + dy
               if self.is_in_field(nx, ny) and self.field[ny][nx] == TREE:
                  if random.random() < 0.3:  # 30% шанс распространения
                     self.field[ny][nx] = BURNING_TREE
                     new_burning_trees.append({'x': nx, 'y': ny, 'burn_time': 5})
         else:
            new_burning_trees.append(fire)
      
      self.burning_trees = new_burning_trees
   
   def update_weather(self):
      """Обновление погодных условий"""
      self.weather_duration -= 1
      
      if self.weather_duration <= 0:
         # Меняем погоду
         weathers = ['sunny', 'rainy', 'stormy']
         weights = [70, 20, 10]  # Вероятности
         
         self.weather = random.choices(weathers, weights=weights)[0]
         self.weather_duration = random.randint(10, 30)
         self.clouds = []
         
         print(f"\n🌤️  Погода изменилась: {self.weather}")
         
         if self.weather == 'rainy':
            print("🌧️  Идет дождь! Пожары тухнут медленнее.")
         elif self.weather == 'stormy':
            print("⛈️  Начинается гроза! Осторожно с молниями!")
               
         self.generate_clouds()
   
   def is_in_field(self, x, y):
      """Проверка, что координаты в пределах поля"""
      return 0 <= x < self.width and 0 <= y < self.height
   
   def collect_water(self):
      """Верток берет воду с реки"""
      x, y = self.helicopter.x, self.helicopter.y
      if self.field[y][x] == WATER and self.water_level < self.water_capacity:
         self.water_level = self.water_capacity
         print("💧 Резервуар наполнен водой!")
         return True
      return False
   
   def extinguish_fire(self):
      """Тушение пожара"""
      if self.water_level > 0:
         x, y = self.helicopter.x, self.helicopter.y
         if self.field[y][x] == BURNING_TREE:
            # Тушим пожар
            self.field[y][x] = TREE
            self.water_level -= 1
            
            # Удаляем из списка горящих деревьев
            self.burning_trees = [f for f in self.burning_trees if not (f['x'] == x and f['y'] == y)]
            
            self.score += 20
            print(f"✅ Пожар в ({x}, {y}) потушен! +20 очков")
            return True
      else:
         print("❌ Нет воды в резервуаре!")
      return False
   
   def visit_hospital(self):
      """Посещение госпиталя"""
      x, y = self.helicopter.x, self.helicopter.y
      if (x, y) == self.hospital_pos and self.lives < 3:
         if self.score >= 50:
            self.score -= 50
            self.lives = 3
            print("🏥 Здоровье восстановлено! -50 очков")
            return True
         else:
            print("❌ Недостаточно очков для лечения (нужно 50)")
      return False
   
   def visit_shop(self):
      """Посещение магазина улучшений"""
      x, y = self.helicopter.x, self.helicopter.y
      if (x, y) == self.shop_pos:
         print("\n🛒 Магазин улучшений:")
         print(f"1. Увеличить вместимость воды (+1) - 100 очков")
         print(f"2. Выйти из магазина")
         
         choice = input("Выберите улучшение: ")
         
         if choice == '1' and self.score >= 100:
            self.score -= 100
            self.water_capacity += 1
            self.water_level = self.water_capacity  # Автоматически наполняем
            print(f"✅ Вместимость воды увеличена до {self.water_capacity}!")
            return True
         elif choice == '1':
            print("❌ Недостаточно очков (нужно 100)")
      
      return False
   
   def check_game_over(self):
      """Проверка условий конца игры"""
      if self.lives <= 0:
         self.game_over = True
         print("\n💀 ИГРА ОКОНЧЕНА! Закончились жизни.")
         return True
      
      # Победа, если потушены все пожары и их нет какое-то время
      if len(self.burning_trees) == 0 and self.tick > 50:
         if random.random() < 0.01:  # 1% шанс на победу после 50 тиков без пожаров
            self.game_won = True
            print("\n🎉 ПОБЕДА! Все пожары потушены, лес спасен!")
            return True
      
      return False
   
   def render(self):
      """Отрисовка игрового поля"""
      os.system('cls' if os.name == 'nt' else 'clear')
      
      print("=" * 50)
      print("🚁 ВЕРТОЛЕТ-ПОЖАРНЫЙ")
      print("=" * 50)
      
      # Статистика
      print(f"Очки: {self.score} | Жизни: {'❤️ ' * self.lives}")
      print(f"Вода: {'💧' * self.water_level}{'○' * (self.water_capacity - self.water_level)}")
      print(f"Погода: {self.weather.upper()} | Тик: {self.tick}")
      print(f"Горящих деревьев: {len(self.burning_trees)}")
      print()
      
      # Легенда
      print("Легенда: · пусто | 🌲 дерево | 🔥 пожар | 🪵 пепел")
      print("        🌊 вода | 🚁 вертолет | 🏥 госпиталь | 🛒 магазин")
      print("=" * 50)
      
      # Отрисовка поля
      field_copy = [row.copy() for row in self.field]
      
      # Добавляем облака и молнии
      for cloud in self.clouds:
         if self.is_in_field(cloud['x'], cloud['y']):
            field_copy[cloud['y']][cloud['x']] = cloud['type']
      
      # Добавляем вертолет
      field_copy[self.helicopter.y][self.helicopter.x] = HELICOPTER
      
      # Рисуем поле
      for y in range(self.height):
         row = ''
         for x in range(self.width):
            row += field_copy[y][x] + ' '
         print(row)
      
      print("=" * 50)
      print("Управление: WASD - движение, E - взять воду, F - тушить")
      print("          H - госпиталь, M - магазин, Q - выход")
      print("=" * 50)
   
   def update(self):
      """Основной игровой цикл"""
      self.tick += 1
      
      # Обновляем пожары
      self.update_fires()
      
      # Может начаться новый пожар
      if self.weather != 'rainy':  # В дождь пожары реже
         self.start_fire()
      
      # Обновляем погоду
      self.update_weather()
      
      # Проверяем конец игры
      self.check_game_over()
   
   def save_game(self, filename='game/savegame.json'):
      """Сохранение игры"""
      save_data = {
         'width': self.width,
         'height': self.height,
         'field': self.field,
         'helicopter': {
               'x': self.helicopter.x,
               'y': self.helicopter.y
         },
         'score': self.score,
         'lives': self.lives,
         'water_capacity': self.water_capacity,
         'water_level': self.water_level,
         'tick': self.tick,
         'burning_trees': self.burning_trees,
         'weather': self.weather,
         'weather_duration': self.weather_duration,
         'hospital_pos': self.hospital_pos,
         'shop_pos': self.shop_pos,
         'timestamp': datetime.now().isoformat()
      }
      
      with open(filename, 'w', encoding='utf-8') as f:
         json.dump(save_data, f, ensure_ascii=False, indent=2)
      
      print(f"✅ Игра сохранена в {filename}")
   
   def load_game(self, filename='game/savegame.json'):
      """Загрузка игры"""
      try:
         with open(filename, 'r', encoding='utf-8') as f:
            save_data = json.load(f)
         
         self.width = save_data['width']
         self.height = save_data['height']
         self.field = save_data['field']
         self.helicopter.x = save_data['helicopter']['x']
         self.helicopter.y = save_data['helicopter']['y']
         self.score = save_data['score']
         self.lives = save_data['lives']
         self.water_capacity = save_data['water_capacity']
         self.water_level = save_data['water_level']
         self.tick = save_data['tick']
         self.burning_trees = save_data['burning_trees']
         self.weather = save_data['weather']
         self.weather_duration = save_data['weather_duration']
         self.hospital_pos = tuple(save_data['hospital_pos'])
         self.shop_pos = tuple(save_data['shop_pos'])
         
         print(f"✅ Игра загружена из {filename}")
         print(f"   Сохранение от: {save_data['timestamp']}")
         return True
         
      except FileNotFoundError:
         print(f"❌ Файл сохранения {filename} не найден")
         return False
      except Exception as e:
         print(f"❌ Ошибка при загрузке: {e}")
         return False
   
   def run(self):
      """Запуск игры"""
      print("🚁 Добро пожаловать в игру 'Вертолет-пожарный'!")
      print("=" * 50)
      
      # Генерация мира
      self.generate_rivers()
      self.generate_trees()
      self.generate_hospital()
      self.generate_shop()
      
      # Начальная позиция вертолета
      while True:
         x = random.randint(0, self.width - 1)
         y = random.randint(0, self.height - 1)
         if self.field[y][x] == EMPTY:
            self.helicopter.x = x
            self.helicopter.y = y
            break
      
      # Главный игровой цикл
      while not self.game_over and not self.game_won:
         self.render()
         self.update()
         
         # Обработка ввода
         action = input("Действие: ").lower()
         
         if action == 'q':
            save = input("Сохранить игру перед выходом? (y/n): ").lower()
            if save == 'y':
               self.save_game()
            print("👋 До свидания!")
            break
         elif action == 's':
               self.save_game()
               continue
         elif action == 'l':
               if self.load_game():
                  continue
         elif action in ['w', 'a', 's', 'd']:
            # Движение вертолета
            dx, dy = 0, 0
            if action == 'w':
               dy = -1
            elif action == 's':
               dy = 1
            elif action == 'a':
               dx = -1
            elif action == 'd':
               dx = 1
            
            new_x = self.helicopter.x + dx
            new_y = self.helicopter.y + dy
            
            if self.is_in_field(new_x, new_y):
               self.helicopter.x = new_x
               self.helicopter.y = new_y
            else:
               print("❌ Нельзя выйти за пределы карты!")
               self.lives -= 1
               print(f"💔 Потеряна жизнь! Осталось: {self.lives}")
         elif action == 'e':
            self.collect_water()
         elif action == 'f':
            self.extinguish_fire()
         elif action == 'h':
            self.visit_hospital()
         elif action == 'm':
            self.visit_shop()
         else:
            print("❌ Неизвестная команда")
         
         # Небольшая пауза для отрисовки
         time.sleep(0.1)
      
      # Конец игры
      if self.game_over or self.game_won:
         self.render()
         print("\n" + "=" * 50)
         if self.game_won:
            print(f"🎉 ПОБЕДА! Ваш счет: {self.score}")
         else:
            print(f"💀 ИГРА ОКОНЧЕНА! Ваш счет: {self.score}")
         print("=" * 50)
         
         replay = input("Сыграть еще раз? (y/n): ").lower()
         if replay == 'y':
            # Создаем новую игру
            new_game = Game(self.width, self.height)
            new_game.run()

class Helicopter:
   def __init__(self, x=0, y=0):
      self.x = x
      self.y = y

def main():
   """Точка входа в программу"""
   print("🚁 ВЕРТОЛЕТ-ПОЖАРНЫЙ")
   print("=" * 50)
   print("1. Новая игра")
   print("2. Загрузить игру")
   print("3. Выход")
    
   choice = input("Выберите действие: ")
    
   if choice == '1':
      # Настройка размера поля
      try:
         width = int(input("Ширина поля (10-40): ") or 20)
         height = int(input("Высота поля (8-20): ") or 10)
         width = max(10, min(width, 40))
         height = max(8, min(height, 20))
      except ValueError:
         width, height = 20, 10
         print("Используется размер по умолчанию 20x10")
      
      game = Game(width, height)
      game.run()
   elif choice == '2':
      game = Game()
      if game.load_game():
         game.run()
   elif choice == '3':
      print("👋 До свидания!")
   else:
      print("❌ Неверный выбор")

if __name__ == "__main__":
   main()