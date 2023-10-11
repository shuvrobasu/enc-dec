import os
import random
import time
import msvcrt

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def generate_random_character():
    return chr(random.randint(33, 126))

def generate_random_line(length):
    return ''.join(generate_random_character() for _ in range(length))

def matrix_screen(rows, cols, speed, times):
    running = True
    for _ in range(times):
        matrix = [generate_random_line(cols) for _ in range(rows)]
        for line in matrix:
            print(f"\x1b[1;32m{line}\x1b[0m")
            time.sleep(speed)
            if msvcrt.kbhit():
                key = msvcrt.getch().decode()
                if key.lower() == ' ':
                    running = False
                    break
                else:
                    running = False
                    break
        if not running:
            break
        clear_screen()

# # Adjust these parameters as you like
# rows = 15
# cols = 50
# speed = 0.05  # Adjust the speed of the effect
# x = 5  # Number of times to display the matrix
#
# matrix_screen(rows, cols, speed, x)
