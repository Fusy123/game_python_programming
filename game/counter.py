# Считалка
# Демонстрация range
print("Посчитаем")
for i in range(10):
    print(i, end=" ")
print("\n\n Перечислим кратные 5: ")
for i in range(0, 50, 5):
    print(i, end=" ")
print("\n\n В обратном порядке: ")
for i in range(10, 0, -1):
    print(i, end=" ")
input("\n\nНажмите ENTER чтобы выйти. \n")
