my_list = [1, 2, 3, 4, 5]
flag = 0
for i in range(len(my_list)):
    if 3 in my_list:
        print("Element Found")
        flag = 1
        break
if flag == 0:
    print("Element not found")
