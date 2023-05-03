num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num_one = 0
num_two = 0
if num1 < num2:
    num_one = num1
else:
    num_one = num2
if num3 < num4:
    num_two = num3
else:
    num_two = num4
if num_one < num_two:
    print(num_one)
else:
    print(num_two)