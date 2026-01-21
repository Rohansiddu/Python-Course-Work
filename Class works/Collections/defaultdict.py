from collections import defaultdict
n=[1,2,1,1,2,2,3,4,2,4,3,4,5,2,4,1,2,4,6,5,6,5,4,7]
res=defaultdict(int)
for i in n:
    res[i]+=1
print(res)