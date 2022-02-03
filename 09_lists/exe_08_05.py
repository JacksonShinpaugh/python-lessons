f = input('File name: ')
file = open(f)
count = 0

for line in file :
    line = line.rstrip()
    if not 'From ' in line :
        continue

    else :
        sline = line.split()
        count = count + 1
        print(sline[1])

print("There were", count, "lines in the file with From as the first word")

