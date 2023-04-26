num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = (num % 1000) // 100
digit0 = num // 1000
print("Цифра в позиции тысяч равна", digit0)
print("Цифра в позиции сотен равна", digit1)
print("Цифра в позиции десятков равна", digit2)
print("Цифра в позиции единиц равна", digit3)