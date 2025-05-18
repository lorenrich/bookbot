'''
Bookbot bootdev project

main.py will serve as the entry point to our program and include any code that doesn't fit elsewhere
'''
# Import
from stats import *
import sys

def get_book_text(filepath):
    # Take the filepath as an input and return the contents of the file as a string
    with open(filepath) as f:
        text = f.read()
        return text

def main():
    # Use the contents from get_book_text and print to console with the relative path
    file_contents = get_book_text(filepath)

    print(file_contents)


'''
Get input from user to run program
'''
# If sys.argv doesn't have two entries, print an error message
try:
    sys.argv
    # Set the filepath as the second sys argument ([0] is the script name)
    filepath = sys.argv[1]
except Exception:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)


'''
Call functions and print the report
'''
text = get_book_text(filepath)

char = count_characters(text)

# Print  report
print("============ BOOKBOT ============")
print(f"Analyzing book found at {filepath}...")

print("----------- Word Count ----------")

get_num_words(text)

print('--------- Character Count -------')

sort_dictionary(char)

print('============= END ===============')