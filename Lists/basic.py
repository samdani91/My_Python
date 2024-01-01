my_list = []
my_list_2 = list()
size = int(input("Enter the size:"))
for i in range(size):
    ele = int(input())
    my_list.append(ele)
print(my_list)
my_list.append(1412)
print(my_list)
print("New size:", len(my_list))
print("Last element:", my_list[-1])  # -1 -2 -3 from the end of the list
last_ele = my_list.pop()
print(last_ele)
print(my_list)
