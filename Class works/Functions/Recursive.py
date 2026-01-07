"""def display(n):
    if n==11:
        return
    print(n)
    display(n+1)
    # print(n)
display(1)"""

'''def display(ind):
    if ind==len(s):
        return
    print(s[ind])
    display(ind+1)
s='Python Programing'
display(0)'''


'''def display(ind):
    if ind==len(s):
        return
    print(s[:ind+1])
    display(ind+1)
s='abcdef'
display(0)'''

# a
# ab
# abc
# abcd
# abcde
# abcdef


'''def display(ind,n):
    if ind == len(s)-n+1:
        return
    print(s[ind:ind+n])
    display(ind+1,n)
s='abcdef'
display(0,2)

# ab
# bc
# cd
# de
# ef
'''

'''def shoot(bullets):
    if bullets==0:
        print("You are dead!!...")
        return
    print(f'{bullets} left')
    shoot(bullets-1)
shoot(10)

# 10 left
# 9 left
# 8 left
# 7 left
# 6 left
# 5 left
# 4 left
# 3 left
# 2 left
# 1 left
# You are dead!!...'''


def ad(n):
    if n==0:
        return 0
    return n+ad(n-1)
    
print(ad(10))