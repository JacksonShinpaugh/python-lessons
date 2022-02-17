fhand = input('Enter File: ')
f = open(fhand)

count = dict()

for line in f :

    if not line.startswith('From ') :
        continue
    word = line.split()
    count[word[1]] = count.get(word[1], 0) + 1

bigcount = None
bigword = None

for k, v in count.items() :
    if bigword is None or v > bigcount :
        bigword = k
        bigcount = v


print(bigword, bigcount)

            


        

        



        


        
        



        
