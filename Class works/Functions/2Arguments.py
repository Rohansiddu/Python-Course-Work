#Positonal arguments
'''def display(uname,email,password):
    print(f'username: {uname} \n email: {email} \n password: {password}')
username=input()
mail=input()
pwd=input()
display(username,mail,pwd)'''
#Key arguments
'''def display(uname,email,password):
    print(f' username: {uname} \n email: {email} \n password: {password}')
username=input()
mail=input()
pwd=input()
display(uname=username,email=mail,password=pwd,end='\n')
display(email=mail,uname=username,password=pwd)
display(password=pwd,uname=username,email=mail)'''

#default arguments
#default must be at the end of the arguments
'''def display(uname,email,password,status="Absent"):     
    print(f'username: {uname} \n email: {email} \n password: {password} \n status: {status}')
display("ABCD",'ABCD@gmail.com','ABCD1234!')
display("EFGH",'EFGH@gmail.com',"EFGH1234",'Present')'''

#for not fixed args
'''def display(*names):
    #print(names)
    for i in names:
        print(i,end=" ")
    print()
display('a','b','c','d')
display('s','t','o')
display('e','f','g','h','i')'''


#assingned as dictonaties
def display(**names):
    #print(names)
    for i in names:
        print(f'{i}:{names[i]}')
    print()
display(k1='a',k2='b',k3='c',k4='d')
display(n1='s',n2='t',n3='o')
display(x1='e',x2='f',x3='g',x4='h',x5='i')