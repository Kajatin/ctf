import base64
import codecs

key = base64.b64decode('c3ludCB2ZiA6IGEwX29icWxfczBldHJnX2RlX3BicXI=')
key = key.decode('utf-8')

flag = codecs.decode(key, 'rot_13')
print(flag.split(' ')[-1])