OPERATIONS = {
    '🍡': 'add',
    '🤡': 'clone',
    '📐': 'divide',
    '😲': 'if_zero',
    '😄': 'if_not_zero',
    '🏀': 'jump_to',
    '🚛': 'load',
    '📬': 'modulo',
    '⭐': 'multiply',
    '🍿': 'pop',
    '📤': 'pop_out',
    '🎤': 'print_top',
    '📥': 'push',
    '🔪': 'sub',
    '🌓': 'xor',
    '⛰': 'jump_top',
    '⌛': 'exit'
}


if __name__ == '__main__':
    with open('program', 'r') as fin:
        with open('program_decoded', 'w') as fout:
            for line in fin:
                line_replacement = ''
                for char in line:
                    repl = OPERATIONS.get(char) or char
                    line_replacement += repl
                fout.writelines([line_replacement])