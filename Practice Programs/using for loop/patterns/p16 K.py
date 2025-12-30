n=int(input())
for row in range(n):
    for col in range(n):
        if col == 0 or (col==(n-1-row) and row<n//2) or (col==(row-1) and row>=n//2):
            print('*',end=' ')
        else:
            print('',end=' ')
    print()

#  0 1 2 3 
#0 *     *
#1 *   *
#2 * * 
#3 *   *
#4 *     *

# 0 3
# 1 2
# 2 1
# 3 2
# 4 3