from Crypto.Util.number import inverse

# given in competition
e = 1
c = 9327565722767258308650643213344542404592011161659991421
n = 245841236512478852752909734912575581815967630033049838269083

# factorized 'n' at http://factordb.com/
p = 416064700201658306196320137931
q = 590872612825179551336102196593

# decode rsa
phi = (q-1) * (p-1)
d = inverse(e, phi)
m = pow(c, d, n)

flag = bytes.fromhex(hex(m)[2:])
print(flag.decode('utf-8'))