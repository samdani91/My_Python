ages = {'Samdani': 22, 'Nafiz': 26, 'Partha': 21, 'Afifa': 12, 'Arisha': 10}
print(ages)
print(ages['Samdani'])
ages['Samdani'] += 8
print(ages)

# print using for each
for key in ages:
    value = ages[key]
    print(key + " -> " + str(value))

# functions
print(ages.keys())
print(ages.values())
print(ages.items())

print("Length:", len(ages))

print("Poped:", ages.pop('Samdani'))
print(ages)

del ages['Nafiz']
print(ages)

ages.clear()
print(ages)

# adding
phone = {}
phone['Samdani'] = '01842775898'
phone['Oni'] = None
print(phone)
