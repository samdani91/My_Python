# unordered but no duplicate
# set_1 = {}  # this is wrong because this is empty dec of dict
my_set = set()
my_set_2 = {1412, 1, 5, 8, 4, 1, 5, 9}

my_set.add(1)
my_set.add(1)
my_set.add(2)
my_set.add(2)

print(my_set)
print(my_set_2)

print(len(my_set))
print(len(my_set_2))

print(my_set.intersection(my_set_2))
print(my_set.difference(my_set_2))
print(my_set.union(my_set_2))

print(my_set)

print(1412 in my_set)
print(1 in my_set_2)