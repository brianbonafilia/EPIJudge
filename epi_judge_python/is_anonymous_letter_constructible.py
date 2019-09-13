import collections
from test_framework import generic_test


def is_letter_constructible_from_magazine(letter_text, magazine_text):
    # TODO - you fill in here.
    letters = collections.defaultdict(int)
    for letter in magazine_text:
        letters[letter] += 1
    for letter in letter_text:
        letters[letter] -= 1
        if letters[letter] < 0:
            return False
    return True


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main("is_anonymous_letter_constructible.py",
                                       'is_anonymous_letter_constructible.tsv',
                                       is_letter_constructible_from_magazine))
