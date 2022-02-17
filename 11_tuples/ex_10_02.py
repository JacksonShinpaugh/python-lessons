#open and load mbox-short.txt
#open dict
#iterate through lines with 'From '
#index to pinpoint the hour message was sent
#count instances of each hour
#print counts, sorted by hour


#open/load file
from audioop import reverse


fname = input('Enter file: ')
if len(fname) < 1:
    name = 'mbox-short.txt'
f = open(fname)

#open dict
di = {}

for lin in f:
    lin = lin.rstrip()
    
    if lin.startswith('From '):
        words = lin.split()
        hour = words[5].split(':')[0]
        di[hour] = di.get(hour, 0) + 1

print(di.items())

lst = list()
for k,v in di.items():
    new = (k,v)
    lst.append(new)

lst = sorted(lst)
for k,v in lst:
    print(k,v)
        
        

        
