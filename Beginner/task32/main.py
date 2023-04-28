num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = (num % 1000) // 100
digit0 = num // 1000
sum_one = digit0 + digit3
sum_two = digit1 - digit2
if sum_one == sum_two:
    print("ДА")
else:
    print("НЕТ")