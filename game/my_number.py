# Игра Отгадай число
# Компьютер должен отгадать случайное число от 1 до 100
# Игроку надо загадать число от 1 до 100
# предложение больше/меньше или угадали
import random

print("\tДобро пожаловать в игру \" Угадай число\" !")
print("\nВам нужно загадать число от 1 до 100")

tries = 0
the_number = random.randint(1, 100)
min_number = 1
max_number = 100

while True:
    your_number = int(input('Введите загаданное число: '))
    if 1 <= your_number <= 100:
        break
    else:
        print("Вы ввели неправильное число!")

while your_number != the_number:
    print(f"Компьютер думает что ваше число {the_number}")
    print(f"Если ваше число больше {the_number}? нажмите '1', если меньше, нажмите '2'")
    tries += 1
    while True:
        answer = int(input("Ваш ответ: "))
        if answer == 1:
            min_number = the_number + 1
            break
        elif answer == 2:
            max_number = the_number - 1
            break
        else:
            print("вы ввели не правильное число!")
    the_number = int((min_number + max_number) / 2)

print(f"Я отгадал ваше число за {tries} попыток, Это число {the_number}")
