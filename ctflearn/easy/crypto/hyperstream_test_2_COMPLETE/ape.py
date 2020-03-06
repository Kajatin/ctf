bacon_to_ascii = {
    'aaaaa': 'a',
    'aaaab': 'b',
    'aaaba': 'c',
    'aaabb': 'd',
    'aabaa': 'e',
    'aabab': 'f',
    'aabba': 'g',
    'aabbb': 'h',
    'abaaa': '(i/j)',
    'abaab': 'k',
    'ababa': 'l',
    'ababb': 'm',
    'abbaa': 'n',
    'abbab': 'o',
    'abbba': 'p',
    'abbbb': 'q',
    'baaaa': 'r',
    'baaab': 's',
    'baaba': 't',
    'baabb': '(u/v)',
    'babaa': 'w',
    'babab': 'x',
    'babba': 'y',
    'babbb': 'z'
}

code = 'ABAAAABABAABBABBAABBAABAAAAAABAAAAAAAABAABBABABBAAAAABBABBABABBAABAABABABBAABBABBAABB'.lower()

ascii_string = ''.join([bacon_to_ascii.get(key) for key in [code[i:i+5] for i in range(0,len(code),5)]])
print(ascii_string.upper())