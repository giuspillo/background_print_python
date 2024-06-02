# bprint stays for Background Print
# it just prints a text with a different background color, useful to
# (a) keep track of what happens during code execution
# (b) make the output a little more cute :3

def bprint_yellow(text : str):
    print(f"\033[0;30;43m{text}\033[0m")

def bprint_blue(text : str):
    print(f"\033[0;30;44m{text}\033[0m")

def bprint_red(text : str):
    print(f"\033[0;30;41m{text}\033[0m")

def bprint_green(text : str):
    print(f"\033[0;30;42m{text}\033[0m")

# examples

# common messages
bprint_blue(f'Loaded data')
bprint_blue(f'Starting training of the model...')

# success
exec_time = 709
bprint_green(f'\nCompleted in {exec_time}ms')

# errors
bprint_red(f'\nError during evaluation')

# warning or similar
bprint_yellow(f'\n(Your model sucks)')