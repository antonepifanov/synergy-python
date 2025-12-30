class Turtle:    
   def __init__(self, x, y, s):
      self.x = x
      self.y = y
      self.s = s
      print(f"Создана черепашка в позиции ({x}, {y}) с шагом {s}")
    
   def go_up(self):
      self.y += self.s
    
   def go_down(self):
      self.y -= self.s
    
   def go_left(self):
      self.x -= self.s
    
   def go_right(self):
      self.x += self.s
    
   def evolve(self):
      self.s += 1
    
   def degrade(self):
      if self.s <= 1:
         raise ValueError(f"Невозможно уменьшить шаг! Текущий шаг: {self.s}, минимальный шаг: 1")
        
      self.s -= 1
    
   def count_moves(self, x2, y2):
      # Вычисляем разницу
      dx = abs(x2 - self.x)
      dy = abs(y2 - self.y)
        
      # Вычисляем необходимое количество ходов по каждой оси
      moves_x = (dx + self.s - 1) // self.s if self.s > 0 else 0
      moves_y = (dy + self.s - 1) // self.s if self.s > 0 else 0
        
      # Общее количество ходов
      total_moves = moves_x + moves_y
      
      print(f"От ({self.x}, {self.y}) до ({x2}, {y2}) с шагом {self.s}")
      print(f"Нужно ходов: {total_moves} ({moves_x} по X, {moves_y} по Y)")
      
      return total_moves
   
# Создаем черепашку
x = int(input("Введите начальное положение по оси x: "))
y = int(input("Введите начальное положение по оси y: "))
s = int(input("Введите начальное количество клеточек: "))
t = Turtle(x, y, s)
   
# Считаем ходы до точки
x2 = int(input("Введите конечное положение по оси x: "))
y2 = int(input("Введите конечное положение по оси y: "))
moves = t.count_moves(x2, y2)
print(f"Минимальное количество ходов: {moves}")