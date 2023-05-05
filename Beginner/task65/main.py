num = int(input())
a = num % 10
b = (num % 100) // 10
c = num // 100
max_num = max(a, b, c)
min_num = min(a, b, c)
avg_num = (a + b + c) - (max_num + min_num)
if max_num - min_num == avg_num:
    print("Число интересное")
else:
    print("Число неинтересное")