fhand = open('mbox-short.txt')
for line in fhand :
    line = line.rstrip()
    line = line.upper()
    print(line)
