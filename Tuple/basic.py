# tuple is immutable but list is mutable

# mutable
list_1 = [1, 2, 3, 4, 5, 6, 7, 8]
list_2 = list_1

print(list_1)
print(list_2)

list_1[0] = 1412

print(list_1)
print(list_2)

print()
# immutable
my_tuple = ()  # empty tuple
my_tuple_2 = tuple()  # empty tuple
tuple_1 = (1, 2, 3, 4, 5, 6, 7, 8)
tuple_2 = (1, 2, 3, 4, 5, 6, 7)

print(tuple_1)
print(tuple_2)

tuple_1[0] = 1412  # this is wrong

print(tuple_1)
print(tuple_2)
