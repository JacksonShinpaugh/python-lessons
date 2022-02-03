f = input('Enter file name: ')
file = open(f)
list = list()

for line in file :
    line = line.split()
    print(line)

    for word in line :
        if word in list :
            continue
        list.append(word)
   
list.sort()
print(list)
   


  
    
        


