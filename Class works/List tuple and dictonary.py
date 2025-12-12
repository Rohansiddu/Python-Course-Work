#list
'''
b=[]
a=[[],[],[]]  #nested list
l=list()

'''

l=[1,5,3,4,2]
a=[5,6,7,8]
'''
print(l+a)
print((l+a)*56)
print(3 in a)
print(4 not in l)
print(l[1],a[3])
print(l[-2]+l[0])
print(l[:3]) #need not to mention starting point for the start
print(l[-1:-4:-1]) #-1 for the reverse of the list and negitive values are the count from the back wards
print(l[::-1])
'''

#Update
'''
a[2]='9'
print(a)
print(id(l))
'''

#Add at the end

'''
l.append('yoo')
print(l)
a.append(9)
print(a)
'''

#Insert at a index place
'''
l.insert(0,34)
print(l)
'''

#Extend (adds multiple names at once end of the list)
'''
l.extend([11,22,33,55,99,77])
print(l)
'''
#remove a perticular element value input
'''
l.remove('yoo')
print(l)
'''

#remove a perticular element by index number
'''
l.pop(0)
print(l)

l.pop() #pop the last element
print(l)
'''
#delete  __it deletes completly the value from the memory location
'''
del l(0)
print(l)
'''
#clear   _wipes every element in the list
'''
l.clear()
print(l)'''


'''print(l.index('yoo'))  #finding the index number

print(l.count(5))  #counting repitation of  a pirticular element
'''

'''
l.sort()  #it effects the original list
print(l)'''

'''
print(sorted(l))    #it wont effect the original list
''' 

'''print(len(l))

print(sum(a)) #only works when the list contining numeric values or float values
any(a) #used to check if any values in the list are true or not
all(a)  #used to check if all values in the list are true or not'''

#tuple

    #immutable, ordered collection of elements
    #tuples are faseter thean lists because it is immutable
  #t=()
  #t=tuple()
  #t=(1,2,3,4)
  #t=(1,1.1,'string',[],(),{},{1,2,3})

'''t=(1,2,3)
s=(2,3,4)
print(t+s)
print(4 in t)
print(3 in s)'''

'''
lang=('java','python','html','ruby','css')
print(lang[2])
print(lang[-3])

print(lang[::])

print(lang[:3])

print(lang[::2])

print(lang[-3::])

print(lang[-3:-1:])

print(lang[-3::-1])'''



#packing and unpacking
"""
z=1,2,3,4       #default considered as tuple
print(type(a))
a,b,c,d=z
print(d)

user1='rohan','rohansiddusamudrala@zohomail.in','rohan000'
uname,mail,password=user1
print(uname,mail)
print(f" User-name:\n\t{uname} \n mail: \n\t{mail} \n password: \n\t{password}")
"""


'''t=(1,2,[5,9],3)
print(t[0])
t[2].append(0)
print(t)'''

#Dictonary
'''d={}
d={1:2,2:3,3:4}
print(2 in d) #works only for the keys 
print(d[2])'''

'''data={'name':'subhash','batchno':44,'course':'python full stack'}
print(data['name'])
print(data.get('age'))
print(data.get('age',"Key went to tour"))'''

#Set default search for the key if not there it appends the key to the dictonary
'''data.setdefault('age',21)
print(data)
print(data.setdefault('name'))
print(data)'''
