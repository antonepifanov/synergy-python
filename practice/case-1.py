from datetime import date

# --- Шаблоны цифр 5 строк x 4 столбца (последний столбец — пробел-разделитель) ---
DIGITS = {
   '0': ["*** ", "* * ", "* * ", "* * ", "*** "],
   '1': [" *  ", "**  ", " *  ", " *  ", "*** "],
   '2': ["*** ", "  * ", "*** ", "*   ", "*** "],
   '3': ["*** ", "  * ", "*** ", "  * ", "*** "],
   '4': ["* * ", "* * ", "*** ", "  * ", "  * "],
   '5': ["*** ", "*   ", "*** ", "  * ", "*** "],
   '6': ["*** ", "*   ", "*** ", "* * ", "*** "],
   '7': ["*** ", "  * ", "  * ", "  * ", "  * "],
   '8': ["*** ", "* * ", "*** ", "* * ", "*** "],
   '9': ["*** ", "* * ", "*** ", "  * ", "*** "],
   ' ': ["    ", "    ", "    ", "    ", "    "],
}

def input_date():
   """Запрашивает дату рождения и возвращает datetime.date (не в будущем)."""
   while True:
      try:
         d = int(input("День рождения (число): "))
         m = int(input("Месяц рождения (число от 1 до 12): "))
         y = int(input("Год рождения (например, 2005): "))
         birth = date(y, m, d)
         if birth > date.today():
            print("Дата не может быть в будущем, попробуйте снова.\n")
            continue
         return birth
      except ValueError:
         print("Некорректная дата, попробуйте снова.\n")

def weekday_name(d: date) -> str:
   """Возвращает название дня недели для даты."""
   names = ["Понедельник", "Вторник", "Среда", "Четверг", "Пятница", "Суббота", "Воскресенье"]
   return names[d.weekday()]

def is_leap_year(year: int) -> bool:
   """Високосный ли год."""
   return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def calculate_age(birth: date) -> int:
   """Полных лет на сегодня."""
   today = date.today()
   age = today.year - birth.year
   # если день рождения в этом году ещё не наступил — минус год
   if (today.month, today.day) < (birth.month, birth.day):
      age -= 1
   return age

def print_stars(text: str):
   """Печатает строку (цифры и пробелы) звёздочками построчно."""
   rows = [""] * 5
   for ch in text:
      pattern = DIGITS[ch]
      for i in range(5):
         rows[i] += pattern[i]
   for r in rows:
      print(r)

def main():
   birth = input_date()
   print(f"\nДата рождения: {birth.strftime('%d.%m.%Y')}")
   print(f"День недели: {weekday_name(birth)}")
   print(f"Високосный год: {'да' if is_leap_year(birth.year) else 'нет'}")
   print(f"Возраст: {calculate_age(birth)} лет")

   print("\nДата звёздочками:")
   print_stars(birth.strftime("%d %m %Y"))

if __name__ == "__main__":
   main()