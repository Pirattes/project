list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
new_list = [list_1[i] for i in range(1, len(list_1)) if list_1[i] > list_1[i - 1]]
print(new_list)
