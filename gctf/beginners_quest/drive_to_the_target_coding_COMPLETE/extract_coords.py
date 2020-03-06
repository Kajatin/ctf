fout = open('coords.txt', 'w')

with open('output.txt', 'r') as fin:
    for line in fin.readlines():
        if 'fast' in line or 'flag' in line:
            continue

        coords = line.split(',')[1:3]
        coords = ','.join(coords)
        fout.write(coords+'\n')

fout.close()