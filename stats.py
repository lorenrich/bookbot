'''
Bookbot bootdev project

stats.py will contain the functions for analyzing text
'''

def get_num_words(text):
    words = text.split()
    num_words = len(words)
    print(f"Found {num_words} total words")


def count_characters(text):
    # List the characters which appear and the number of times they are used
    lower = text.lower()

    letters = []
    counts = []

    for letter in lower:
        # Skip non-alphabetical characters
        if letter.isalpha():
            if letter not in letters:
                letters.append(letter)

    for letter in letters:
        count = lower.count(letter)
        counts.append(count)

    count_dict = dict(zip(letters, counts))
   
    return count_dict


def sort_dictionary(count_dict):

    list = []
    for key, value in count_dict.items():
        list.append({'char': key, 'num': value})

    # Sort from largest character count to smallest
    list.sort(key=lambda x: x['num'], reverse=True)

    # Change output of list
    for item in list:
        print(f"{item['char']}: {item['num']}")