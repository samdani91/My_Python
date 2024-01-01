arr = [10, 6, 9, 4, 5, 1, 0]

arr.reverse()  # reverse the list only not reversely sorted
print(arr)

# arr.sort()    #ascending order altering the original list
print(sorted(arr))  # ascending order without altering the original list
arr.sort(reverse=True)
print(arr)
