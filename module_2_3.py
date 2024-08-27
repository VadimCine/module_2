my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
len_list = len(my_list)
a = int(0)
while a != len_list:
    if my_list[a] > 0:
        print(my_list[a])
        a += int(1)
        continue
    elif my_list[a] == 0:
        a += int(1)
        continue
    break


