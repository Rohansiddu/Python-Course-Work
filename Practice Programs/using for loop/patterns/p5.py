n=int(input())
for i in range(n):
    for j in range((n-1)-i):
        print(' ',end=' ')
    for k in range(i+1):
        print('*',end=' ')
    print()
#   0 1 2 3 4
# 0         * 
# 1       * *
# 2     * * *
# 3   * * * *
# 4 * * * * *

# 0 4 1
# 1 3 2
# 2 2 3
# 3 1 4
# 4 0 5