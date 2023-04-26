number = int(input())
sum3 = number % 10
sum2 = (number // 10) % 10
sum1 = number // 100
print("Сумма цифр =", sum1 + sum2 + sum3)
print("Произведение цифр =", sum1 * sum2 * sum3)