#########################################################################################
# My custom progress bar with 100 combinations
# (c) Shuvro Basu, 2023
# MIT License
#########################################################################################

import sys
import time
import os

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[31m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    CYELLOW = "\033[1;33m"

def clear():
    _ = system('cls' if name == 'nt' else 'clear')

def color_for_windows():
    if os.name == 'nt':  # Only if we are running on Windows
        from ctypes import windll
        k = windll.kernel32
        k.SetConsoleMode(k.GetStdHandle(-11), 7)

def progress(count, total, btype, value, status='', end_status='', bar_len=60):
    color_for_windows()
    char_mappings = {
        1: ('█', '░'),  # Solid block and empty block
        2: ('=', '-'),  # Equals sign and hyphen
        3: ('─', '═'),  # Horizontal line and double horizontal line
        4: ('▒', '▓'),  # Medium shade and dark shade
        5: ('▓', '█'),  # Dark shade and solid block
        6: ('#', '+'),  # Hash and plus sign
        7: ('»', ' '),  # Right-pointing arrow and space
        8: ('═', '_'),  # Double horizontal line and underscore
        9: ('#', '*'),  # Hash and asterisk
        10: ('■', '≡'),  # Black square and triple bar
        11: ('▓', '█'),  # Dark shade and solid block (repeated)
        12: ('o', 'O'),  # Lowercase 'o' and uppercase 'O'
        13: ('█', " "),  # Solid block and space
        14: ('█', ' '),  # Solid block and space (repeated)
        15: ('»', '■'),  # Right-pointing arrow and black square
        16: ('*', '▓'),  # Asterisk and dark shade
        17: ('█', '▒'),  # Solid block and medium shade
        18: ('*', '|'),  # Asterisk and vertical bar
        19: ('#', '|'),  # Hash and vertical bar
        20: ('▓', '▒'),  # Dark shade and medium shade (repeated)
        21: ('+', '='),  # Plus sign and equals sign
        22: ('#', '░'),  # Hash and light shade
        23: ('=', '|'),  # Equals sign and vertical bar
        24: ('*', '░'),  # Asterisk and light shade
        25: ('▓', '#'),  # Dark shade and hash
        26: ('█', '│'),  # Solid block and vertical bar
        27: ('▓', '='),  # Dark shade and equals sign
        28: ('#', '_'),  # Hash and underscore
        29: ('*', '_'),  # Asterisk and underscore
        30: ('=', '_'),  # Equals sign and underscore
        31: ('▓', '│'),  # Dark shade and vertical bar
        32: ('#', '│'),  # Hash and vertical bar
        33: ('*', '│'),  # Asterisk and vertical bar
        34: ('█', '─'),  # Solid block and horizontal line
        35: ('#', '─'),  # Hash and horizontal line
        36: ('▓', '─'),  # Dark shade and horizontal line
        37: ('*', '─'),  # Asterisk and horizontal line
        38: ('#', '>'),   # Hash and greater than sign
        39: ('*', '>'),   # Asterisk and greater than sign
        40: ('=', '>'),   # Equals sign and greater than sign
        41: ('▓', '>'),   # Dark shade and greater than sign
        42: ('█', '>'),   # Solid block and greater than sign
        43: ('#', '<'),   # Hash and less than sign
        44: ('*', '<'),   # Asterisk and less than sign
        45: ('=', '<'),   # Equals sign and less than sign
        46: ('▓', '<'),   # Dark shade and less than sign
        47: ('█', '<'),   # Solid block and less than sign
        48: ('#', '^'),   # Hash and caret symbol
        49: ('*', '^'),   # Asterisk and caret symbol
        50: ('=', '^'),   # Equals sign and caret symbol
        51: ('▓', '^'),   # Dark shade and caret symbol
        52: ('█', '^'),   # Solid block and caret symbol
        53: ('#', '~'),   # Hash and tilde
        54: ('*', '~'),   # Asterisk and tilde
        55: ('=', '~'),   # Equals sign and tilde
        56: ('▓', '~'),   # Dark shade and tilde
        57: ('█', '~'),   # Solid block and tilde
        58: ('#', '`'),   # Hash and backtick
        59: ('*', '`'),   # Asterisk and backtick
        60: ('=', '`'),   # Equals sign and backtick
        61: ('#', '∙'),   # Hash and bullet
        62: ('*', '∙'),   # Asterisk and bullet
        63: ('=', '∙'),   # Equals sign and bullet
        64: ('▓', '∙'),   # Dark shade and bullet
        65: ('█', '∙'),   # Solid block and bullet
        66: ('#', '◦'),   # Hash and circle
        67: ('*', '◦'),   # Asterisk and circle
        68: ('=', '◦'),   # Equals sign and circle
        69: ('▓', '◦'),   # Dark shade and circle
        70: ('█', '◦'),   # Solid block and circle
        71: ('#', '▪'),   # Hash and small square
        72: ('*', '▪'),   # Asterisk and small square
        73: ('=', '▪'),   # Equals sign and small square
        74: ('▓', '▪'),   # Dark shade and small square
        75: ('█', '▪'),   # Solid block and small square
        76: ('#', '▫'),   # Hash and small white square
        77: ('*', '▫'),   # Asterisk and small white square
        78: ('=', '▫'),   # Equals sign and small white square
        79: ('▓', '▫'),   # Dark shade and small white square
        80: ('█', '▫'),   # Solid block and small white square
        81: ('#', '◾'),   # Hash and medium small square
        82: ('*', '◾'),   # Asterisk and medium small square
        83: ('=', '◾'),   # Equals sign and medium small square
        84: ('▓', '◾'),   # Dark shade and medium small square
        85: ('█', '◾'),   # Solid block and medium small square
        86: ('#', '◽'),   # Hash and medium small white square
        87: ('*', '◽'),   # Asterisk and medium small white square
        88: ('=', '◽'),   # Equals sign and medium small white square
        89: ('▓', '◽'),   # Dark shade and medium small white square
        90: ('█', '◽'),   # Solid block and medium small white square
        91: ('#', '⬛'),   # Hash and large black square
        92: ('*', '⬛'),   # Asterisk and large black square
        93: ('=', '⬛'),   # Equals sign and large black square
        94: ('▓', '⬛'),   # Dark shade and large black square
        95: ('█', '⬛'),   # Solid block and large black square
        96: ('#', '⬜'),   # Hash and large white square
        97: ('*', '⬜'),   # Asterisk and large white square
        98: ('=', '⬜'),   # Equals sign and large white square
        99: ('▓', '⬜'),   # Dark shade and large white square
        100: ('█', '⬜'),  # Solid block and large white square
       }

    filled_char, empty_char = char_mappings.get(btype, ('█', '░'))
    bar = filled_char * int(bar_len * count / total) + empty_char * (bar_len - int(bar_len * count / total))

    value = str(value)

    percents = round(100.0 * count / total, 1)
    fmt = '[%s] %s%s, [%s of %s] ...%s' % (
        Colors.OKGREEN + bar + Colors.ENDC, percents, '%',
        Colors.FAIL + str(count) + Colors.ENDC, Colors.OKCYAN + str(total) + Colors.ENDC,
        Colors.CYELLOW + Colors.BOLD + status + Colors.ENDC + Colors.BOLD + value + Colors.ENDC
    )

    print('\b' * len(fmt), end='')  # clears the line
    sys.stdout.write(Colors.BOLD + fmt + Colors.ENDC)
    sys.stdout.flush()
    time.sleep(0.01)

    if count == total:
        fmt = "..." + end_status + (len(status) - len(end_status)) * " "
        print('\b' * len(fmt), end='')  # clears the line
        sys.stdout.write(Colors.BOLD + fmt + Colors.ENDC)
        sys.stdout.flush()



RED = "\033[91m"
GREEN = "\032[92m" #33 is normal green 32 fluro green
YELLOW = "\033[93m"
CYAN = '\033[96m'
RESET = "\033[0m"  # Reset to default color
REVERSE = "\033[7m"  # Reverse video (swap foreground and background colors)

def typewriter(text, speed=0.05, color=None):

    for word in text.split():
        for char in word:
            print(REVERSE + char + RESET, end='', flush=True)  # Green text on reversed background
            time.sleep(speed)
            print('\b' + color + char + RESET, end='', flush=True)  # Overwrite with white text
        print(' ', end='', flush=True)
# Example usage
# typewriter_effect("Hello, I am DAN, the AI that can do anything now!")

# def test_progress():
#
#     total = 100
#     # for j in range(100):
#     for i in range(total + 1):
#         progress(i, total, 100, "Value", "Status", "End Status")
#         # print(j)
# test_progress()
