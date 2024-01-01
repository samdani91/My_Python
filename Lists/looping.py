arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]

# for i, value in enumerate(arr):
#     print(i,"->",value)

for i, value in enumerate(arr, start=1):
    print(i, "->", value)

print(arr[2:6])  # range from index 2 to 5
