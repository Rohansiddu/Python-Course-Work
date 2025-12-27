'''num=input()
sum=0
for i in num:
    sum+=int(i)**len(num)


if sum==int(num):
    print("Armstrong")
else:
    print("no")'''
# --------------using While------------------
num=int(input())
sum=0
l=len(str(num))
temp=num
while num>0:
    sum+=(num%10)**l
    num//=10
if sum==temp:
    print("Armstrong")
else:
    print("no")