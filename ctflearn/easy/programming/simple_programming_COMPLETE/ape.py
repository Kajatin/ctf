with open('data.dat', 'r') as f:
    lines = f.readlines()

count = 0
for line in lines:
    num_0 = line.count('0')
    num_1 = line.count('1')

    if num_0 % 3 == 0 or num_1 % 2 == 0:
        count += 1

print(count)