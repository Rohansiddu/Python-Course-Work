s='Python programming'
print(s.split()) #by default spaces as splitter
print(s.split('r'))
print(s.split('o'))

print(s.rsplit(' '))
print(s.rsplit(' ',1))

a='''hey
world, 
here
i
am'''
print(a.splitlines()) #split by lines

#partition

b= 'Dhanush is a good boy'
print(b.partition(' '))
print(b.rpartition(' '))

c= '1.python_operators.py'
print(c.partition('.'))
print(c.rpartition('.'))

#Join

j='a','b','c','d'
print(''.join(j))
print(','.join(j))
print('.'.join(j))
print('   '.join(j))
print('\n'.join(j))
