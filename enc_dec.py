#######################################################################################################################
# My own implementation of the Ceaser Cypher Encrryption
# Fast and easy to use
# Not decode-able by online decoders
# Can be used for moderately sensitive information.
# The encoding process works by using the length of each word in text and adding 1 as shift value to the length
# then a constant shift value of 5 is used to re-encode the text
# At the end, a base64 encoding is done on the text encoded text.
# Thus there are three levels of encryption which makes this pretty strong.
# Note : encryption may cause formatting to be lost (Lf/Cr) and won't be recovered at decryption time.
# Additional functions added from the original version 1 above
# ver 1.1
# =======
# added function to show the files with serial numbers for enc/dec if user didnt enter a file name when F option used
# ver 1.2
# =======
# added chunk size functionality so that large files can be broken into chunks depedning on size and then processed making
# the alogrithm work twice as fast
# ver 1.3
# =======
# added an undocumented functionality to delete files either txt or bnc when R option is used in first prompt. This will
# permanently delete the files without having to manually delete. Multiple files can be deleted by using the corresponding
# serial number of the files separated by comma.
######################################################################################################################

import base64
import os
import sys
import color_text as ct                  #my custom color formats and inputs
import progress_bars as pv               #my custom progress bar with 100+ progress bars
import matrix                            #my own simulated matrix splash screen :-)

SHIFT = 5
input_text = ""
input_file = ""
EXTENSION = '.BNC'
VER = "ver. 1.3"
RUNONCE = False
#matrix config
rows = 20
cols = 75
speed = 0.01
times = 5
NUMCHUNKS = 0

banner = """
___________                     ________                   
\_   _____/  ____    ____       \______ \    ____   ____   
 |    __)_  /    \ _/ ___\ ______|    |  \ _/ __ \_/ ___\  
 |        \|   |  \\  \___/_____/|    `   \\  ___/\  \___  
/_______  /|___|  / \___  >     /_______  / \___  >\___  > 
        \/      \/      \/              \/      \/     \/  
                                                           """

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            ascii_offset = ord('a') if char.islower() else ord('A')
            result += chr((ord(char) - ascii_offset + shift) % 26 + ascii_offset)
        else:
            result += char
    return result

def format_file_size(file_size):
    for unit in ['B', 'KB', 'MB', 'GB', 'TB']:
        if file_size < 1024.0:
            return f"{file_size:.2f} {unit}"
        file_size /= 1024.0
    return f"{file_size:.2f} PB"  # Petabytes and beyond


def process_file_chunks(input_file, output_file, process_function, shift):
    with open(input_file, 'rb') as file:
        file_size = os.path.getsize(input_file)
        chunk_size = determine_chunk_size(file_size)
        num_chunks = (file_size + chunk_size - 1) // chunk_size
        ct.print_yellow(f"File size: {format_file_size(file_size)}.")
        ct.print_yellow(f"Chunk size: {chunk_size} bytes")
        ct.print_yellow(f"Number of chunks: {num_chunks}")

        for i in range(num_chunks):

            start = i * chunk_size
            end = min((i+1) * chunk_size, file_size)
            file.seek(start)
            data = file.read(end - start)
            pv.progress(i+1, num_chunks, 14 , "Processing...", "Pass 1...", "Completed")

            processed_data = process_function(data, shift)
            with open(output_file, 'ab') as output:
                output.write(processed_data)
        print()

def encrypt_chunk(chunk, shift):
    encrypted_chunk = b""
    for byte in chunk:
        encrypted_byte = (byte + shift) % 256
        encrypted_chunk += bytes([encrypted_byte])
    return encrypted_chunk

def decrypt_chunk(chunk, shift):
    decrypted_chunk = b""
    for byte in chunk:
        decrypted_byte = (byte - shift) % 256
        decrypted_chunk += bytes([decrypted_byte])
    return decrypted_chunk


def encrypt_file(input_file, output_file):
    process_file_chunks(input_file, output_file, encrypt_chunk, SHIFT)

def decrypt_file(input_file, output_file):
    process_file_chunks(input_file, output_file, decrypt_chunk, SHIFT)

def decrypt_text(text):
    try:
        text = base64.b64decode(text).decode()
    except base64.binascii.Error:
        print("Error: Incorrect padding. Please ensure the input is correctly encoded.")
        return ""
    text = caesar_cipher(text, -5)
    # print(text)
    # wait()
    words = text.split()
    decrypted_text = ""
    total = len(words) # for progress bar
    i = 1
    for word in words:
        shift = len(word) + 1
        pv.progress(i, total, 1, "Decrypting...", "Pass 1...", "Completed")
        i = i + 1

    #    print()
        ct.print_lgreen("Pass 2...")
        decrypted_word = caesar_cipher(word, -shift)
        decrypted_text += decrypted_word + " "
        ct.print_lgreen("Pass 2... Completed.")

    print()
    return decrypted_text.strip()


#encrypt text input
def encrypt_text(text):
    words = text.split()
    encrypted_text = ""
    total = len(words)
    i =1
    for word in words:
        shift = len(word) + 1
        encrypted_word = caesar_cipher(word, shift)
        encrypted_text += encrypted_word + " "
        # for i in range(total + 1):
        pv.progress(i, total, 14, "Encrypting...", "Pass 1...", "Completed.")
        i = i + 1

    print() # just a blank line
    ct.print_lgreen("Pass 2...")
    encrypted_text = caesar_cipher(encrypted_text.strip(), 5)
    encrypted_text = base64.b64encode(encrypted_text.encode()).decode()
    ct.print_lgreen("Pass 2...completed.")

    return encrypted_text

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_bnc_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith('.bnc')]
    return files

def list_text_files():
    files = [f for f in os.listdir('.') if os.path.isfile(f) and f.lower().endswith('.txt')]
    return files

def show_text_files():
    files = list_text_files()
    for i, file in enumerate(files, start=1):
        ct.color_underline(f"{[i]}. {file}", 35)

def show_bnc_files():
    files = list_bnc_files()
    for i, file in enumerate(files, start=1):
        # print(f"{i}. {file}")
        ct.color_underline(f"{[i]}. {file}", 35)

def get_valid_choice():
    while True:
        choice = ct.color_reverse("Please enter the number corresponding to the file you want to choose: ", 34)
        if choice.isdigit() and 1 <= int(choice) <= len(list_text_files()):
            return int(choice)
        elif int(choice) == 0:
            return False
        else:
            print("Invalid choice. Please enter a valid number.")

def checkfile(filename):
    if len(filename) == 0:
        ct.print_red("[!]-Filename cannot be blank !")
        wait()
    elif os.path.isfile(filename):
        return True
    else:
        ct.color_underline_text(f"{[filename]} does not exist.", 32)
        wait()
        return False

def showfile():
    global input_file
    ans = ct.color_reverse("Do you want to see the list of files [Y]/[N]? ", 31).lower()
    if ans == 'y':
        show_text_files()
        choice = get_valid_choice()
        chosen_filename = list_text_files()[choice - 1]
        input_file = chosen_filename
        return input_file
    else:
        return False

def showbncfile():
    global input_file
    ans = ct.color_reverse("Do you want to see the list of files [Y]/[N]? ", 31).lower()
    if ans == 'y':
        show_bnc_files()
        choice = get_valid_choice()
        chosen_filename = list_bnc_files()[choice - 1]
        input_file = chosen_filename
        return input_file
    else:
        return False

def clearme():
    for _ in range(22):
        print("\n")

def wait(msg=None):
    if msg == None:
        msg_i = "Press [ENTER/RETURN] key to continue..."
    else:
        msg_i = msg
    a = ct.color_underline_text(msg_i, 35).lower()
    # print(a)
    if a == "i" and len(input_text) > 0:
        p = input()
        ct.color_underline_texte("IOC : " + index_of_coincidence(input_text), 36)
        wait()

def index_of_coincidence(text):
    if len(text) > 0:
        total_chars = len(text)
        frequencies = [0] * 26
        for char in text:
            if char.isalpha():
                char_index = ord(char.lower()) - ord('a')
                frequencies[char_index] += 1
        ioc = sum(freq * (freq - 1) for freq in frequencies) / (total_chars * (total_chars - 1))
        return ioc
    else:
        ct.print_red("Input is empty. Can be done only for keyboard input.")

def myinput(prompt, default_value):
    user_input = input(f"{prompt} [{default_value}]: ")
    if user_input == '':
        return default_value
    else:
        return user_input

def remove_bnc_extension(filename):
    if filename.endswith('.bnc'):
        return filename[:-4]
    else:
        return filename

def determine_chunk_size(file_size):
    if file_size < 1024 * 1024:  # Less than 1MB
        return 512
    else:
        return 1024


#
# def list_and_delete_files(directory):
#     # Get a list of files with extensions .bnc and .txt
#     files = [f for f in os.listdir(directory) if f.endswith(('.bnc', '.txt'))]
#
#     # Display the files with serial numbers
#     for i, file_name in enumerate(files, start=1):
#         print(f"{i}. {file_name}")
#
#     # Ask user for file numbers to delete
#     try:
#         user_input = input("Enter file numbers to delete (comma-separated): ")
#         delete_numbers = [int(num) for num in user_input.split(',')]
#
#         # Validate the user input
#         if all(1 <= num <= len(files) for num in delete_numbers):
#             # Delete the selected files
#             for num in delete_numbers:
#                 os.remove(os.path.join(directory, files[num - 1]))
#             print("Files deleted successfully.")
#             wait()
#         else:
#             print("Invalid file numbers entered.")
#             wait()
#     except ValueError:
#         print("Invalid input. Please enter comma-separated numbers.")
#         wait()

import os


def list_and_delete_files(directory):
    # Ask user for extension
    extension = ct.color_reverse("Enter the file extension (without dot): ",33)

    # Validate the extension
    if extension not in ["bnc", "txt"]:
        print("Invalid extension. Please enter 'bnc' or 'txt'.")
        wait()
        return

    # Get a list of files with the specified extension
    files = [f for f in os.listdir(directory) if f.endswith(f'.{extension}')]

    if len(files) == 0:
        ct.print_red("No files found with the specified extension.")
        wait()
        return
    # Display the files with serial numbers
    for i, file_name in enumerate(files, start=1):
        print(f"{i}. {file_name}")

    # Ask user for file numbers to delete
    try:
        user_input = input("Enter file numbers to delete (comma-separated): ")
        delete_numbers = [int(num) for num in user_input.split(',')]

        # Validate the user input
        if all(1 <= num <= len(files) for num in delete_numbers):
            # Delete the selected files
            for num in delete_numbers:
                os.remove(os.path.join(directory, files[num - 1]))
            print("Files deleted successfully.")
            wait()
        else:
            print("Invalid file numbers entered.")
            wait()
    except ValueError:
        print("Invalid input. Please enter comma-separated numbers.")
        wait()




def main():
    global input_text, RUNONCE, col, rows, speed, times , extensions
    clearme()
    if RUNONCE == False:
        matrix.matrix_screen(rows, cols, speed, times)
        RUNONCE = True
    clearme()

    ct.print_highlight("█" * 120)
    ct.print_blue(banner)
    ct.print_highlight("█" * 120)
    print()
    ct.print_reverse("[Enc]-[Dec]«-"+ "("+VER+")-»")
    ct.print_purple("─"*100)
    ct.print_cyan("(c) Shuvro Basu, 2023.")
    ct.print_red("MIT License. No warranties.")
    ct.print_cyan("═" * 100)
    choice = ct.color_reverse("Enter [E] to encrypt or [D] to decrypt ([Blank] to exit): ", 34).lower()

    if choice == 'e':
        input_type = ct.color_reverse("Enter [F] to use a file or [T] to enter text: ", 34).lower()
        if input_type == 'f':
            input_file = ct.color_reverse("Enter the name of the file to [Encrypt] : ", 35)
            if checkfile(input_file):

                output_file = input_file + ".bnc"
                ct.print_highlight("[!] Processing... " + output_file)
                encrypt_file(input_file, output_file)
                ct.print_green(f"File '{input_file}' encrypted and saved as '{output_file}'.")
                wait()
            else:
                input_file = showfile()
                if input_file:
                    output_file = myinput("Enter the name of the output file: ", input_file + ".bnc")
                    if output_file.endswith('.bnc'):
                        ct.print_highlight("Processing... " + output_file)
                        encrypt_file(input_file, output_file)
                        ct.print_green(f"File '{input_file}' encrypted and saved as '{output_file}'.")
                        wait()
                else:
                    ct.print_red("No input file selected")
                    wait()
                    return False

        elif input_type == 't':
            input_text = input("Enter the text to encrypt: ")
            if len(input_text) == 0:
                ct.color_underline("[Invalid] input or[blank].", 31)
                wait()
            else:
                encrypted_text = encrypt_text(input_text)
                ct.print_yellow("Encrypted Text: " + encrypted_text)
                wait()
        else:
            ct.color_underline("Invalid input type. Please enter [F] or[ T].", 31)
            wait()
    elif choice == 'd':
        input_type =  ct.color_reverse("Enter [F] to use a file or [T] to enter text: ", 34).lower()

        if input_type == 'f':
            input_file = ct.color_reverse("Enter the name of the [decrypted] file: ", 34)
            if input_file.endswith('.bnc'):
                if checkfile(input_file):
                    output_file = remove_bnc_extension(input_file)
                    ct.print_highlight("Decrypting..." + input_file)
                    decrypt_file(input_file, output_file)
                    ct.print_green(f"File '{input_file}' decrypted and saved as '{output_file}'.")
                    wait()
            else:
                input_file = showbncfile()
                if input_file:
                    output_file = remove_bnc_extension(input_file)
                    output_file = myinput("Enter the name of the output file: ", input_file + ".txt")
                    if output_file.endswith('.txt'):
                        ct.print_highlight("Processing... " + output_file)
                        decrypt_file(input_file, output_file)
                        ct.print_green(f"File '{input_file}' decrypted and saved as '{output_file}'.")
                        wait()
                else:
                    ct.print_red("No input file selected.")
                    wait()
                    return False
        elif input_type == 't':
            input_text = input("Enter the text to decrypt: ")
            if len(input_text) == 0:
                ct.color_underline("[Invalid] input or [blank].", 31)
                wait()
            else:
                decrypted_text = decrypt_text(input_text)
                ct.print_yellow("Decrypted Text: " + decrypted_text)
                wait()
        else:
                ct.color_underline("Invalid input type. Please enter [F] or [T].", 31)
                wait()

    elif choice == 'r':
            list_and_delete_files("./")
    elif choice == "\n" or len(choice) == 0 or choice == "":
            ct.print_red("Exiting...")
            pv.typewriter("Thank you for using Enc-Dec.", 0.10, color=pv.CYAN)
            sys.exit(0)
    elif choice == "i":
        ct.print_purple("IOC : [" + str(index_of_coincidence(input_text)) + "]")
        wait()
    else:
       ct.color_underline("Invalid choice. Please enter [E] or [D].", 31)
       wait()

if __name__ == "__main__":
    while True:
        clear_screen()
        main()
