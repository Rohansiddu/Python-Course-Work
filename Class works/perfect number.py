#check if a number is perfect or not,the sum of factors are equal to the number is called perfect number
n=int(input("Enter the number: "))
sum=0
for i in range(1,n//2+1):
    if n%i==0:
        print(i)
if sum==n:
    print("Perfect Number")
else:
    print("Not a Perfect Number")
    