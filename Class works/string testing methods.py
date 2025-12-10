s='python programming'
print(s.startswith('p'))
print(s.startswith('a'))

print(s.endswith('g'))
print(s.endswith('a'))

print('Rohan'.isalpha())      #contining only alphabets and numbers
print('555'.isalpha())      

print('Rohan'.islower())
print('rohan'.islower())
print('Rohan'.isupper())
print('ROHAN'.isupper())

print(' '.isspace())
print('Rohan Vs Harsha'.istitle())
print('Rohan vs Harsha'.istitle()) #all hve to start with a capital letter

print('myvar'.isidentifier())
print('_myvar'.isidentifier())
print('12myvar'.isidentifier())

print('9'.isdecimal()) #isdecimal allows only 0-9
print('26²'.isdigit()) #isdigit allows only powers
print('Ⅱ'.isnumeric()) #numeric allows only numbers from any language