n=int(input())
for i in range(n):
    for j in range(n-i):
        print('*',end=' ')
    print()


#   0 1 2 3 4
# 0 * 
# 1 * * 
# 2 * * *
# 3 * * * *
# 4 * * * * *