# Симулятор трехлетнего ребенка
# демонстрация бесконечного цикла, пока не введешь "Потому что" цикл не остановится
print("\tДобро пожаловать в программу \" Симулятор трехлетнего ребенка\" \n")
print("Имитация разговора с маленьким ребенком.")
print("Попробуйте остановить этот кошмарю \n")
response = ""
while response != "Потому что":
    response = input("Почему? \n")
print("А, ладно.")