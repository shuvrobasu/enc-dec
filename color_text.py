import os
import sys

#Few text formatting functions:
def color_for_windows():
    if os.name == 'nt':  # Only if we are running on Windows
        from ctypes import windll
        k = windll.kernel32
        k.SetConsoleMode(k.GetStdHandle(-11), 7)


def print_lgreen(text):

    os.system("")
    print("\033[1;32m" + text + "\033[m")

def print_reverse(text):
    os.system("")
    print("\033[7m" + text + "\033[m")

def print_highlight(text):
    """
    Print text in a highlighted format.
    """
    os.system("")
    print("\033[97m" + text + "\033[m")

def print_red(text):
    """
    Print text in red.
    """
    os.system("")
    print("\033[91m" + text + "\033[m")

def print_green(text):
    """
    Print text in green.
    """
    os.system("")
    print("\033[92m" + text + "\033[m")

def print_yellow(text):
    """
    Print text in yellow.
    """
    os.system("")
    print("\033[93m" + text + "\033[m")

def print_blue(text):
    """
    Print text in blue.
    """
    os.system("")
    print("\033[94m" + text + "\033[m")

def print_purple(text):
    """
    Print text in purple.
    """
    os.system("")
    print("\033[95m" + text + "\033[m")

def print_cyan(text):
    """
    Print text in cyan.
    """
    os.system("")
    print("\033[96m" + text + "\033[m")


def color_reverse(predefined, color):
    def apply_format(char, format_code):
        return f"\033[{format_code}m{char}\033[0m"

    pre_defined_text = predefined #"This is an [example] of colored and underlined text."
    formatted_text = ""

    i = 0
    while i < len(pre_defined_text):
        if pre_defined_text[i] == "[":
            end_index = pre_defined_text.find("]", i)
            if end_index != -1:
                inner_text = pre_defined_text[i + 1:end_index]
                formatted_text += apply_format(inner_text, f"7;{color};1")  # Underline, specified color, Bold
                i = end_index + 1
                continue
        formatted_text += pre_defined_text[i]
        i += 1

    sys.stdout.write(formatted_text)
    sys.stdout.flush()

    user_input = input()
    # print(f"You entered: {user_input}")

    return user_input

def color_underline_text(predefined, color):
    def apply_format(char, format_code):
        return f"\033[{format_code}m{char}\033[0m"

    pre_defined_text = predefined #"This is an [example] of colored and underlined text."
    formatted_text = ""

    i = 0
    while i < len(pre_defined_text):
        if pre_defined_text[i] == "[":
            end_index = pre_defined_text.find("]", i)
            if end_index != -1:
                inner_text = pre_defined_text[i + 1:end_index]
                formatted_text += apply_format(inner_text, f"4;{color};1")  # Underline, specified color, Bold
                i = end_index + 1
                continue
        formatted_text += pre_defined_text[i]
        i += 1

    sys.stdout.write(formatted_text)
    sys.stdout.flush()

    user_input = input()
    # print(f"You entered: {user_input}")

    return user_input


def color_bold(text, color):
    #"\033[1m"

    def apply_format(char, format_code):
        return f"\033[{format_code}m{char}\033[0m"

    formatted_text = ""
    i = 0
    while i < len(text):
        if text[i] == "[":
            end_index = text.find("]", i)
            if end_index != -1:
                inner_text = text[i+1:end_index]
                formatted_text += apply_format(inner_text, f"5;{color};1")  # Underline, Red, Bold
                i = end_index + 1
                continue
        formatted_text += text[i]
        i += 1

    print(formatted_text)


def color_underline(text, color):
    def apply_format(char, format_code):
        return f"\033[{format_code}m{char}\033[0m"

    formatted_text = ""
    i = 0
    while i < len(text):
        if text[i] == "[":
            end_index = text.find("]", i)
            if end_index != -1:
                inner_text = text[i+1:end_index]
                formatted_text += apply_format(inner_text, f"4;{color};1")  # Underline, Red, Bold
                i = end_index + 1
                continue
        formatted_text += text[i]
        i += 1

    print(formatted_text)

# Example Usage:
# # color_and_underline_text("This is an [example] of colored and underlined text.",33)
#
# def test_color_for_windows():
#   cv.color_for_windows()
#
# def test_print_lgreen():
#     cv.print_lgreen("This is a test message in light green.")
#
# def test_print_reverse():
#     cv.print_reverse("This is a test message in reverse color.")
#
# def test_print_highlight():
#     cv.print_highlight("This is a test message in highlighted format.")
#
# def test_print_red():
#     cv.print_red("This is a test message in red.")
#
# def test_print_green():
#     cv.print_green("This is a test message in green.")
#
# def test_print_yellow():
#     cv.print_yellow("This is a test message in yellow.")
#
# def test_print_blue():
#     cv.print_blue("This is a test message in blue.")
#
# def test_print_purple():
#     cv.print_purple("This is a test message in purple.")
#
# def test_print_cyan():
#     cv.print_cyan("This is a test message in cyan.")
#
# def test_color_reverse():
#     user_input = cv.color_reverse("This is an [example] of colored and underlined text.", 33)
#     print(f"You entered: {user_input}")
#
# def test_color_underline_text():
#     user_input = cv.color_underline_text("This is an [example] of colored and underlined text.", 33)
#     print(f"You entered: {user_input}")
#
# def test_color_bold():
#     cv.color_bold("This is an [example] of colored and bold text.", 31)
#
# def test_color_underline():
#     cv.color_underline("This is an [example] of colored and underlined text.", 31)
#
# test_color_for_windows()
# test_print_lgreen()
# test_print_reverse()
# test_print_highlight()
# test_print_red()
# test_print_green()
# test_print_yellow()
# test_print_blue()
# test_print_purple()
# test_print_cyan()
# test_color_reverse()
# test_color_underline_text()
# test_color_bold()
# test_color_underline()
# test_clear_screen()
