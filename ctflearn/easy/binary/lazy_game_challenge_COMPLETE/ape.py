from pwn import *
context.log_level = 'critical'

try:
    c = remote('thekidofarcrania.com', 10001)
    print(c.recv())
    c.send('Y\n')
    print(c.recv())
    print(c.recv())
    c.send('500\n')
    print(c.recv())
    print(c.recv())
    print(c.recv())
    print(c.recv())
finally:
    c.close()