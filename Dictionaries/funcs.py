my_dict = {'a': 1, 'b': 2, 'c': 3}
print(my_dict)

print(my_dict['a'])
# print(my_dict['d']) # throws exception
print(my_dict.get('d'))  # show None
print(my_dict.get('d', 'Not Found'))

my_dict['d'] = 4
print(my_dict)

my_dict['a'] += 9
print(my_dict)

my_dict.update({'Name': 'John', 'Age': 22})
print(my_dict)

del my_dict['Name']
print(my_dict)

pop_value = my_dict.pop('Age')
print("Poped value:", pop_value)
print(my_dict)

for key,value in my_dict.items():
    print(key,value)
