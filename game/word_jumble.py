# Анаграммы
# Компьютер выбирает слово и хаотично меняет буквы местами, задача восстановить слово

import random

# Создаем последовательность слов
WORDS = ("питон", "лопата", "динамит", "синхрофазотрон", "гулять", "мечта", "абракадабра")
# выбираем слово
word = random.choice(WORDS)
# создаем переменную для проверки слова
correct = word
# формируем анаграмму, берем рандомно букву из слова и записываем в новое слово, после чего через срезы выдергиваем
# данную букву из слова. и так далее пока не останется букв в слове.
jumble = ""
while word:
    position = random.randrange(len(word))
    jumble += word[position]
    word = word[:position] + word[(position+1):]

# Начало игры
print("""      Игра анаграммы. 
(надо переставить буквы и угадать начальное слово)
(Для выхода нажмите ENTER, не вводя совей версии)""")

print("загаданное слово: ", jumble)
guess = input("\nПопробуйте угадать слово: ")
user_help_counter = 0
victory_points = len(correct)
while guess != correct and guess != "":
    print("Вы не угадали!")
    user_help = input("Вам нужна подсказка? Да/Нет: ")
    if user_help.lower() == "да":
        user_help_counter += 1
        victory_points -= 1
        print("Cлово начинается: ", correct[:user_help_counter])
    guess = input("Попробуйте угадать слово: ")
if guess == correct:
    print("Вы угадали! Поздравляем!\n")
    print("Вы заработали ", victory_points, "победных очков")
print("Спасибо за игру!")
input("\n\nНажмите ENTER чтобы выйти")

