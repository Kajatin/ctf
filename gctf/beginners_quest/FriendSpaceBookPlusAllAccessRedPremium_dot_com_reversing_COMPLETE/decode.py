from itertools import chain
from sympy import isprime

def cvt_to_char(a,b):
    return chr(b ^ a)

# these arrays are recovered from the program file
in_val = [
    106,
    119,
    113,
    119,
    49,
    74,
    172,
    242,
    216,
    208,
    339,
    264,
    344,
    267,
    743,
    660,
    893,
    892,
    1007,
    975,
    10319,
    10550,
    10503,
    11342,
    11504,
    12533,
    12741,
    12833,
    13437,
    13926,
    13893,
    14450,
    14832,
    15417,
    15505,
    16094,
    16285,
    16599,
    16758,
    17488,
]

in_val2 = [
    93766,
    93969, 
    94440,
    94669,
    94952,
    94865,
    95934,
    96354,
    96443,
    96815,
    97280,
    97604,
    97850,
    98426,
]

in_val3 = [
    9916239,
    9918082,
    9919154,
    9921394,
    9923213,
    9926376,
    9927388,
    9931494,
    9932289,
    9935427,
    9938304,
    9957564,
    9965794,
    9978842,
    9980815,
    9981858,
    9989997,
    100030045,
    100049982,
    100059926,
    100111100,
    100131019,
    100160922,
    100404094,
    100656111,
    100707036,
    100767085,
    100887990,
    100998966,
    101030055,
    101060206,
    101141058,
]

# generate a list of palindrome primes
A002385 = sorted((n for n in chain((int(str(x)+str(x)[::-1]) for x in range(1, 10**5)), (int(str(x)+str(x)[-2::-1]) for x in range(1, 10**5))) if isprime(n))) # http://oeis.org/A002385

# the offsets are recovered from the program file (last load number of each set)

# range 1
offset = 1 - 1
for a,b in zip(A002385[offset:],in_val):
    print(cvt_to_char(a,b),end='')

# range 2
offset = 99 - 1
for a,b in zip(A002385[offset:],in_val2):
    print(cvt_to_char(a,b),end='')

# range 3
offset = 765 - 1
for a,b in zip(A002385[offset:],in_val3):
    print(cvt_to_char(a,b),end='')

print()


















# def gen_primes():
#     """ Generate an infinite sequence of prime numbers.
#     """
#     # Maps composites to primes witnessing their compositeness.
#     # This is memory efficient, as the sieve is not "run forward"
#     # indefinitely, but only as long as required by the current
#     # number being tested.
#     #
#     D = {}
    
#     # The running integer that's checked for primeness
#     q = 2
    
#     while True:
#         if q not in D:
#             # q is a new prime.
#             # Yield it and mark its first multiple that isn't
#             # already marked in previous iterations
#             # 
#             yield q
#             D[q * q] = [q]
#         else:
#             # q is composite. D[q] is the list of primes that
#             # divide it. Since we've reached q, we no longer
#             # need it in the map, but we'll mark the next 
#             # multiples of its witnesses to prepare for larger
#             # numbers
#             # 
#             for p in D[q]:
#                 D.setdefault(p + q, []).append(p)
#             del D[q]
        
#         q += 1