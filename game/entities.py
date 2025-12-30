class Entity:
   """Базовый класс для всех игровых объектов"""
   def __init__(self, x, y, symbol):
      self.x = x
      self.y = y
      self.symbol = symbol
   
   def move(self, dx, dy):
      """Перемещение объекта"""
      self.x += dx
      self.y += dy
   
   def __str__(self):
      return f"{self.__class__.__name__} at ({self.x}, {self.y})"

class Tree(Entity):
   """Класс дерева"""
   def __init__(self, x, y):
      super().__init__(x, y, '🌲')
      self.health = 100
      self.burning = False
      self.burn_time = 0
   
   def start_burning(self):
      """Дерево начинает гореть"""
      self.burning = True
      self.burn_time = 5
      self.symbol = '🔥'
   
   def extinguish(self):
      """Тушение дерева"""
      self.burning = False
      self.burn_time = 0
      self.symbol = '🌲'
   
   def update(self):
      """Обновление состояния дерева"""
      if self.burning:
         self.burn_time -= 1
         if self.burn_time <= 0:
            self.symbol = '🪵'
            self.burning = False
            return True  # Дерево сгорело
      return False

class River(Entity):
   """Класс реки"""
   def __init__(self, x, y):
      super().__init__(x, y, '🌊')

class Hospital(Entity):
   """Класс госпиталя"""
   def __init__(self, x, y):
      super().__init__(x, y, '🏥')
      self.heal_cost = 50
   
   def heal(self, player):
      """Лечение игрока"""
      if player.score >= self.heal_cost and player.lives < 3:
         player.score -= self.heal_cost
         player.lives = 3
         return True
      return False

class Shop(Entity):
   """Класс магазина"""
   def __init__(self, x, y):
      super().__init__(x, y, '🛒')
      self.upgrades = {
         'water_capacity': 100,
         'fire_resistance': 150,
         'speed': 200
      }