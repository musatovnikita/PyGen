number = int(input())
if number == 0:
    print("зеленый")
elif 1 <= number <= 10 and number % 2 != 0:
    print("красный")
elif 1 <= number <= 10 and number % 2 == 0:
    print("черный")
elif 11 <= number <= 18 and number % 2 != 0:
    print("черный")
elif 11 <= number <= 18 and number % 2 == 0:
    print("красный")
elif 19 <= number <= 28 and number % 2 != 0:
    print("красный")
elif 19 <= number <= 28 and number % 2 == 0:
    print("черный")
elif 29 <= number <= 36 and number % 2 != 0:
    print("черный")
elif 29 <= number <= 36 and number % 2 == 0:
    print("красный")
else:
    print("ошибка ввода")