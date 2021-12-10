# Арсенал Героя
# Работа с кортежами
inventory = ()
# рассмотрим условие
if not inventory:
    print("Вы безоружны")
input("\nНажмите ENTER, чтобы продолжить")
# Создание кортежа
inventory = ("меч",
            "кольчуга",
            "щит",
            "снадобье")
# выведем на печать
print("\nСодержимое кортежа: ")
print(inventory)
# последовательный вывод
print("\n В арсенале: ")
for item in inventory:
    print(item)
input("\nНажмите ENTER, чтобы продолжить")
# найдем длину кортежа
print("В вашем распоряжении ", len(inventory), "предмета/-ов.")
input("\nНажмите ENTER, чтобы продолжить")
# проверка на вхождение (использование оператора in)
if "снадобье" in inventory:
    print("Вы еще поживете")
input("\nНажмите ENTER, чтобы продолжить")
# вывод элемента по индексу
index = int(input("\nВведите индекс предмета: "))
print("Под индексом ", index, "в арсенале лежит ", inventory[index])
input("\nНажмите ENTER, чтобы продолжить")
# выбор предметов по срезу
start = int(input("\nВведите начльный индекс: "))
finish = int(input("Введите конец индекса: "))
print("Срез invenory[ ", start, ":", finish, "] - это", end=" ")
print(inventory[start:finish])
input("\nНажмите ENTER, чтобы продолжить")
# соединение кортежей
chest = ("золото", "драгоценные камни", "слитки")
print("вы нашли сокровища: ")
print(chest)
print("положим их в рюкзак")
inventory += chest
print("Теперь в рюкзаке: ")
print(inventory)
input("\nНажмите ENTER, чтобы продолжить")



