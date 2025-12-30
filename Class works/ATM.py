n=[2000, 500, 100, 50, 10]
amount = int(input("Enter the amount: "))
for i in n:
    if amount>=i:
        t=amount//i
        amount %=i
        print(f'{t} * {i}') 