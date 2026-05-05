number_1 = int(input("Введите первое число: "))
s = input("Введите знак: ")
number_2 = int(input("Введите второе число: "))

if s == "/" and number_2 == 0:
    print("На ноль делить нельзя!")
elif s == "+":
        print("Ваш ответ: ", number_1 + number_2)
elif s == "-":
        print("Ваш ответ: ", number_1 - number_2)
elif s == "/":
        print("Ваш ответ: ", number_1 / number_2)
elif s == "*":
        print("Ваш ответ: ", number_1 * number_2)
else:
        print("Неизвестная операция!")
