"""
You're working on a secret team solving coded transmissions.

Your team is scrambling to decipher a recent message, worried it's a plot to break into a major European National Cake Vault. The message has been mostly deciphered, but all the words are backward! Your colleagues have handed off the last step to you.

Write a function reverse_words() that takes a message as a list of characters and reverses the order of the words in place. ↴

Why a list of characters instead of a string?

The goal of this question is to practice manipulating strings in place. Since we're modifying the message, we need a mutable ↴ type like a list, instead of Python 3.6's immutable strings.

For example:

  message = [ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]

reverse_words(message)

# Prints: 'steal pound cake'
print(''.join(message))

When writing your function, assume the message contains only letters and spaces, and all words are separated by one space.
"""


def reverse_words_in_place(words_list):
    """Takes in a list of characters and reverses the words within it in place"""

    word_start_index = 0
    last_index = len(words_list) - 1

    for i in range(0, len(words_list)):
        if words_list[i] == " " or i == last_index:
            if i == last_index:
                reverse_subsection_list(words_list, word_start_index, i)
                reverse_subsection_list(words_list, 0, last_index)
            else:
                reverse_subsection_list(words_list, 0, i - 1)
                word_start_index = i + 1


def reverse_subsection_list(words_list, start, end):
    """Takes in a list of characters and reverses all characters within given range"""

    left_index = start
    right_index = end

    while left_index < right_index:
        words_list[left_index], words_list[right_index] = words_list[right_index], words_list[left_index]
        left_index += 1
        right_index -= 1
