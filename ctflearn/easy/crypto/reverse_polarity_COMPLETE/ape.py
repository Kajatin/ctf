message = "01000011010101000100011001111011010000100110100101110100010111110100011001101100011010010111000001110000011010010110111001111101"

ascii_string = "".join([chr(int(binary, 2)) for binary in [message[i:i+8] for i in range(0,len(message),8)]])

print(ascii_string)