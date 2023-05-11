str1, str2, str3 = input(), input(), input()
len_str1 = len(str1)
len_str2 = len(str2)
len_str3 = len(str3)
if (2 * len_str2 - len_str3 - len_str1) * (2 * len_str3 - len_str2 - len_str1) * (2 * len_str1 - len_str2 - len_str3) == 0:
    print("YES")
else:
    print("NO")