msg = "Hello World!"
print(msg)
print(msg.upper())
print(msg)
print(msg.lower())

print(len(msg))

multi_line = """This is a
    example of multi-line"""
print(multi_line)

# quote_msg = 'Sam's world'' #This is wrong
quote_msg = 'Sam\'s World'
# quote_msg = "Sam's World"
# quote_msg = 'She said,"I am going to say hello"'
print(quote_msg)

print(msg.count('o'))
print(msg.find('o'))  # index of first instance
print(msg.rfind('o'))  # index of last instance

print(msg.find('z'))  # -1 if not found

msg.replace('World', 'Universe')  # returns a mew string
print(msg)
new_msg = msg.replace('World', 'Universe')
print(new_msg)

greeting = 'Hello'
name = 'Samdani'

# string formatting
message = greeting + ', ' + name + '. Welcome!'
print(message)
message = '{}, {}. Welcome!'.format(greeting, name)  # same as above
print(message)
message = f'{greeting}, {name}. Welcome!'  # fstring
print(message)
message = f'{greeting}, {name.upper()}. Welcome!'  # fstring
print(message)

# print(dir(message))  # it shows all attribute and methods of given data type
# print(help(str))  # details
print(help(str.lower))
