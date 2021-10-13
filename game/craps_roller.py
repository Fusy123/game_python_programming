# Игра Кости
# Генерация случайных чисел
import random

# генерация случайных чисел от 1 до 6 (игральный кубик)
die1 = random.randint(1, 6)
die2 = random.randrange(6) + 1
total = die1 + die2
print(" при броске выпало", die1, "и", die2, "очков в сумме", total)
if total <=9:
    print("Вы проиграли!")
else:
    print("Вы победили!")


input("\n\nНажмите ENTER, чтобы выйти")