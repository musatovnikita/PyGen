num1, num2, num3 = int(input()), int(input()), int(input())
max_num = max(num1, num2, num3)
min_num = min(num1, num2, num3)
avg_num = (num1 + num2 + num3) - (max_num + min_num)
print(max_num)
print(avg_num)
print(min_num)