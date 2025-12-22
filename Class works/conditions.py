# simple if
'''if condition:
    #statement
'''
# if else
'''
if condition:
    #stmts
else:
    #stmts
    '''
#  example
'''data={
    'lohit':'l@123',
    'surya':'b$123',
    'thanmai':'a@wer',
    'swetha':'S@5346'
}
uname,pwd=input("Enter the user name and pasword").split()
if data.get(uname)==pwd:
    print(f'Hello {uname} \nYour login successfull')
else:
    print("incorrect user name and password")'''

# if-else-if
'''
if condition:
    #stmts
elif condition:
    #stmts
elif condition:
    #stmts
else:
    #stmts
'''
# Example

'''ch=input("Enter the char: ")
vol='aeiouAEIOU'
if ch.isalpha():
    if ch.vol:        
elif ch.isdigit():
    print("digit")
else:
    print("special char")
'''
#weekend planer elif

'''amount=int(input("Enter the amount: "))
if amount > 10000:
    print("Trip to Goa")
elif 8000 >= amount <10000:
    print("Clubings")
elif 5000 >= amount <8000:
    print("Cafe")
elif 3000 >= amount <5000:
    print("shopping")
elif 1000 >= amount <3000:
    print("visit local places")
elif 500 >= amount < 1000:
    print("order someting")
else:
    print("go for chai")'''

#Greetings 

'''hrs,min=tuple(map(int,input("Enter time: ").split(':')))
if 0<=hrs<4 and 0 <=min <=59:
    print("it's high time. Betteer go to sleep")
elif 4<=hrs<12 and 0 <=min <=59:
    print("Good morning! Have a great day..")

elif 12<=hrs< 16 and 0 <=min <=59:
    print("Good afternoon! have lunch..")

elif 16<=hrs<21 and 0 <=min <=59:
    print("Good Evening! Have dinner...")

elif 21<=hrs<0 and 0 <=min <=59:
    print("Good night! Scrolling reels")
'''
#whatsapp chat

#nested if else


# if condition:
#     if condition:
#         if condition:
#             #stmnts
#         else:
#             #stmts
#     else:
#         #stmts
# else:
#     #stmts

#example

'''data={
    'lohit':'l@123',
    'surya':'b$123',
    'thanmai':'a@wer',
    'swetha':'S@5346'
}
uname,pwd=input("Enter the user name and pasword").split()
if uname in data:
    if data[uname]==pwd:
        print(f'Welcome {uname}')
    else:
        print("incorrect pssword")
else:
    print("incorrect user name")'''