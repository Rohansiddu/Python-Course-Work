#string

'''name=input("Enter any string")
print(name)
print(type(name))'''


#integer

'''a=int(input("Enter your age"))
print(a,type(a))'''

#float

'''p=float(input("Enter the price of the product: "))
print(p,type(p))
'''
#list

'''names=input("enter the names: ").split()  #list of strings
print(names,type(names))'''

'''inte=list(map(int,input("enter the numbers").split())) #map maps int to every element in the list to convert string to integer
print(inte)'''

'''f=list(map(float,input("enter the prices of the prodicts").split())) #for float
print(f,type(f))
print(type(f[1]))'''

#tuple

'''names=tuple(input("enter the names: ").split())  #tuple of strings
print(names,type(names))

names=tuple(map(int,input("enter the numbers: ").split()))  #list of strings
print(names,type(names))

names=tuple(map(float,input("enter the numbers: ").split()))  #list of strings
print(names,type(names))
'''

#set

'''names=set(input("enter ther values"))
print(names,type(names))

names=set(map(int,input("enter ages").split()))
print(names,type(names))

names=set(map(float,input("enter ages").split()))
print(names,type(names))

data=eval(input("Enter the input: "))
print(data,type(data))'''


#packing and unpacking

'''a,b,c,d=(1,2,3,4)
print(a,b,c,d)
email,pwd=tuple(input("Enter the email and password: ").split())
print(email,pwd)
'''
#print

a=123
b=234.34
c="sdfj"
# print("a=",a,"b=",b,"c=",c,sep='\t',end='........')

# print(f" a={a} \n b={b} \n c={c}")

print('a={} b={} c={}'.format(b,c,a))
print('a={} b={} c={}'.format(a,b,c))
print('a={} b={} c={}'.format(c,b,a))