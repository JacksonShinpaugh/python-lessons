fname = input('Enter File: ')
if len(fname) < 1 : fname = 'romeo.txt'
hand = open(fname)

di = dict()
for lin in hand:
    lin = lin.rstrip()
    # print(lin)
    wds = lin.split()
    # sprint(wds)
    for w in wds:
        
        di[w] = di.get(w,0) + 1
        # print(w, 'new', di[w])
            
        # print(di[w])

print(di)

#find most common word

largest = -1
theword = None 
for k, v in di.items() :
    
    if v > largest :
        largest = v
        theword = k

print('Done', theword, largest)