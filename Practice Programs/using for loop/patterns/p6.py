n=int(input())
for i in range(n):
    if i<=n//2:
        for col in range(i+1):
            print('*',end=" ")
    else:
        for col in range(n-i):
            print('*',end=" ")

    print()

#-----------or----------


n=int(input())
for i in range(n):
    if i<=n//2:
        print('* '*(i+1))
    else:
            print('* '*(n-i))

# * 
# * *
# * * *
# * * * *
# * * * * *
# * * * *
# * * *
# * *
# *