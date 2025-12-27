a,b,c=tuple(map(int,input().split()))
if a==b and b==c:
    print("eq")
elif a!=b and b!=c and c!=a:
    print("sc")
else:
    print("is")