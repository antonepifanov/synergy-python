import random

def create_and_add_matrices(rows, cols, min_val, max_val):
   # Генерируем первую матрицу
   matrix1 = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
   print("Первая матрица")
   for i in matrix1:
      print(i)
   
   # Генерируем вторую матрицу
   matrix2 = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
   print("Вторая матрица")
   for i in matrix2:
      print(i)

   # Складываем матрицы
   result = [[matrix1[i][j] + matrix2[i][j] for j in range(cols)] for i in range(rows)]
   print("Сумма матриц")
   for i in result:
      print(i)

rows = int(input("Количество строк: "))
cols = int(input("Количество столбцов: "))
min_val = int(input("Минимальное значение: "))
max_val = int(input("Максимальное значение: "))
create_and_add_matrices(rows, cols, min_val, max_val)
