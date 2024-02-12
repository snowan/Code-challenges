import sys
import locale

def wc(file_path=None):
    if file_path:
        with open(file_path, 'rb') as file:
            content = file.read()

    line_count = len(content.splitlines())
    char_count = len(content)
    word_count = len(content.split())

    return line_count, word_count, char_count, file_path

def is_multibyte_support():
    current_locale = locale.getlocale(locale.LC_CTYPE)
    return current_locale[1] and 'UTF-8' in current_locale[1]

def print_lines(lines, words, chars, file_path):
    print(f"Lines: {lines}, file path: {file_path}")

def print_words(lines, words, chars, file_path):
    print(f"Words: {words}, file path: {file_path}")

def print_characters(lines, words, characters, file_path):
    print(f"Characters: {characters}, file path: {file_path}")

def print_multibyte_characters(lines, words, characters, file_path):
    if is_multibyte_support():
        print(f"Characters: {characters}, file path: {file_path}")
    else:
        print(f"Multibyte character support not available. Defaulting to -c option.")
        print_characters(characters, file_path)

def print_default(*args):
    print(f"Lines: {args[0]}, Words: {args[1]}, Characters: {args[2]} file path: {args[3]}")

def print_wc_stats(file_path=None, option='-l'):
    try:
        lines, words, characters, file_path = wc(file_path)

        options_dict = {
            '-l': print_lines,
            '-w': print_words,
            '-c': print_characters,
            '-m': print_multibyte_characters
        }

        options_dict.get(option, print_default)(lines, words, characters, file_path)

    except Exception as e:
        print(f"An error occurred: {e}")
        sys.exit(1)

if __name__ == "__main__":
    if len(sys.argv) == 3:
        file_path = sys.argv[2]
        print_wc_stats(file_path, sys.argv[1])
    else:
        print("Usage: cat test.txt | python wc.py [option] [file_path]")
        sys.exit(1)
