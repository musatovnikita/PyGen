str1, str2 = input(), input()
if str1 == "красный" and str2 == "синий" or str1 == "синий" and str2 == "красный":
    print("фиолетовый")
elif str1 == "красный" and str2 == "желтый" or str1 == "желтый" and str2 == "красный":
    print("оранжевый")
elif str1 == "синий" and str2 == "желтый" or str1 == "желтый" and str2 == "синий":
    print("зеленый")
elif str1 == "красный" and str2 == "красный":
    print("красный")
elif str1 == "синий" and str2 == "синий":
    print("синий")
elif str1 == "желтый" and str2 == "желтый":
    print("желтый")
elif str1 or str2 not in("красный", "синий", "желтый"):
    print("ошибка цвета")