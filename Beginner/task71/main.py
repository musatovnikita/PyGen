city1, city2, city3 = input(), input(), input()
len_city1 = len(city1)
len_city2 = len(city2)
len_city3 = len(city3)
max_len_city = max(len_city1, len_city2, len_city3)
min_len_city = min(len_city1, len_city2, len_city3)
if min_len_city == len_city1:
    print(city1)
elif min_len_city == len_city2:
    print(city2)
elif min_len_city == len_city3:
    print(city3)
if max_len_city == len_city1:
    print(city1)
elif max_len_city == len_city2:
    print(city2)
elif max_len_city == len_city3:
    print(city3)