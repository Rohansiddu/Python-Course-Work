n=int(input())
for row in range(n):
    for col in range(n):
        if col == n//2  or (row==n-1 and col<=n//2) or row==0 :
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()