import random as r
print(r.randint(1,6))
print(r.uniform(1,6))
names=['vijay','rohan','harsha','dhanush','abhinov']
print(r.choice(names))
r.seed(100)
print(r.choices(names))
print(names)