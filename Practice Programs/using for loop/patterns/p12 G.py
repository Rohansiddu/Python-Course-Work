n=int(input())
for row in range(n):
    for col in range(n):
        if col == 0 or row==0 or (row ==n-1 and col<=n//2) or (col==n//2 and row>=n//2) or (row==n//2 and col>=n//2) or (col==n-1 and row>=n//2):
            print('*',end=' ')
        else:
            print(' ',end=' ')
    print()