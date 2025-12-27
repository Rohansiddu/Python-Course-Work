hr,mins=tuple(map(int,input().split(':')))
if 0<=hr<12 and 0<=mins<=59:
    print(f'{hr}:{mins} AM')
elif hr==12:
    print(f'{hr}:{mins} PM')
else:
    print(f'{hr-12}:{mins} PM')