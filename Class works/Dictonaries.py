d={'k1':'Tarani','k2':'keerthi','k3':'Ravali'}
#print(d.popitem())
#del d['k1']
# print(d)
# print(d.keys())
# print(d.items())
# print(d.values())
d['k1']='Binod'  #only for one change
print(d)
d.update({'k5':'Vijay','k4':'Rakesh'})  #for updating multiple values
print(d)
print(sorted(d))