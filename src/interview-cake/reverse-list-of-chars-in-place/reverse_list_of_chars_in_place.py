"""
Write a function that takes a list of characters and reverses the letters in place
"""


def reverse_list_of_chars_in_place(char_list):
    """Reverses a list of characters in place"""

    if type(char_list) != list:
        raise TypeError(
            "The argument for revese_list_of_chars_in_place must be a list.")

    start_index = 0
    end_index = len(char_list) - 1

    while start_index < end_index:
        char_list[start_index], char_list[end_index] = char_list[end_index], char_list[start_index]
        start_index += 1
        end_index -= 1
