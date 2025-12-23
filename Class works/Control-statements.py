 #for loop
# for var in seq:      -seq= list, tuple, set, dict, str, range
    # stmts
'''
l=['mohan akhil','rohan siddu','vishnu vardhan','mani kumar']   
for name in l:
    print(name.title())

l={'mohan akhil','rohan siddu','vishnu vardhan','mani kumar'}  
for name in l:
    print(name.title())

#Dictonary
products={
    'Airpods':3000,
    'Headset':4000,
    'S25 ultra':150000,
    'Watch':20000
}
for i in products:
    print(f'{i}, ₹{products[i]}')
   --------------------------------------
s='Python Programming'
vol='aeiouAEIOU'
for i in s:
    if i in vol:
        print(f'{i}--v')
    elif i==' ':
        pass
    else:
        print(f'{i}--**c') '''

#range(start,stop+1,step)      default(0,,1)
'''
tb=int(input("number: "))
for i in range(1,11):
    print(tb*i)'''


'''
l=['Airpods','Watch','headphones','samsung']
for i in range(len(l)):
    print(i+1,l[i])
-------------or------------------------------
l=['Airpods','Watch','headphones','samsung']
for a,i in enumerate(l):
    print(a+1,i)'''

