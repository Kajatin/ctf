# import string

message = "q{vpln'bH_varHuebcrqxetrHOXEj"

# for code in string.printable:
#     decrypted = [chr(ord(char) ^ ord(code)) for char in message]
#     print(''.join(decrypted))

print('Bruteforcing .....\n')
for code in range(10000):
    decrypted = [chr(ord(char) ^ code) for char in message]
    decrypted = ''.join(decrypted)
    if 'flag' in decrypted.lower():
        print(code,end='   ')
        print(decrypted)

# found solution
print('\n-----------------------------------\n')
key = 23
decrypted = [chr(ord(char) ^ key) for char in message]
decrypted = ''.join(decrypted)
print(decrypted)