import re

fhand = input('Enter File: ')
f = open(fhand)

numlist = []


for line in f:
    line = line.rstrip()
    numbers = re.findall('[0-9]+', line)
    if numbers == []: 
        continue
    
    for number in numbers:
        num = int(number)
        numlist.append(num)
    
print(sum(numlist))

