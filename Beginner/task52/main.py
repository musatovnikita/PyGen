num1, num2 = int(input()), int(input())
str = input()
if str == "+":
    print(num1 + num2)
elif str == "-":
    print(num1 - num2)
elif str == "*":
    print(num1 * num2)
elif str == "/":
    if num2 == 0:
        print("На ноль делить нельзя!")
    else:
        print(num1 / num2)
else:
    print("Неверная операция")