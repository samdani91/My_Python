def add_many_numbers(numbers, add):
    for ele in numbers:
        add += ele

    return add


numbers = [1, 2, 3, 4, 5]
add = 0

if numbers:
    print("List is not empty")
else:
    print("List is empty")

result = add_many_numbers(numbers, add)
print("Total sum:", result)
