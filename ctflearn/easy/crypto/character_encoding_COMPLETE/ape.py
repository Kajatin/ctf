from binascii import unhexlify

hex_string = "41 42 43 54 46 7B 34 35 43 31 31 5F 31 35 5F 55 35 33 46 55 4C 7D".replace(' ','')
ascii_string = unhexlify(hex_string).decode("utf-8")
print(ascii_string)