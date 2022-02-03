fhand = open('mbox-short.txt')
count = 0
num = 0.0


for line in fhand :
    line = line.rstrip()
    if not 'X-DSPAM-Confidence:' in line :
        continue
   
    else : 
        find = line.find('0')
        strip = line[find:]
        fstrip = float(strip)
        num = num + fstrip
        count = count + 1

print('Average spam confidence:', num/count)


    


    


