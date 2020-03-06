import operator

letters = 'binaryrefinery'
operations = ['|','&','&','>>','|','^','^','^','&','&','|','|','~']

ops = {
    '>>' : operator.rshift,
    # '^' : operator.pow,
    '^' : operator.xor,
    '|' : operator.or_,
    '&' : operator.and_,
    '~' : operator.invert
}

ascii_code = [ord(letter)**3 for letter in letters]

v = ascii_code[0]
for index in range(len(letters)-1):
    for i in range(index+1,len(letters)):
        op = ops[operations[i-1]]

        if op != operator.invert:
            v = op(v, ascii_code[i])
        else:
            v = op(v)

print(v)