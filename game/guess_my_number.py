# Игра Отгадай число
# Компьютер выбирает случайное число от 1 до 100
# Игроку надо за минимальное количество попыток отгадать его
# предложение больше/меньше или угадали
import random

print("\tДобро пожаловать в игру \" Угадай число\" !")
print("\nЯ загадал число от 1 до 100. ")
print("Постарайся отгадать его за минимальное количество попыток. \n")
the_number = random.randint(1, 100)
guess = int(input("Ваше число: "))
tries = 1
# цикл отгадывания
while guess != the_number:
    if guess > the_number:
        print("Загаданное число меньше вашего")
    else:
        print("Загаданное число больше вашего")
    guess = int(input("Ваше число: "))
    tries += 1
print("вы угадали число! Это действительно число", the_number)
print("Вы отгадали его за ", tries, "попыток")
