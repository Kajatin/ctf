# https://en.wikipedia.org/wiki/Polybius_square

import string
import numpy as np

flag = ''

letters = string.ascii_uppercase.replace('K','')
table = np.array([c for c in letters]).reshape(5,5)
codes = '1-3,4-4,2-1,{,4-4,2-3,4-5,3-2,1-2,4-3,_,4-5,3-5,}'

for code in codes.split(','):
    if '-' not in code:
        flag += code
    else:
        i, j = code.split('-')
        flag += table[int(i)-1,int(j)-1]

print(flag)