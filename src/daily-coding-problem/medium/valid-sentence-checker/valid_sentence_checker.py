"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Nest.

Create a basic sentence checker that takes in a stream of characters and determines whether they form valid sentences. If a sentence is valid, the program should return true.

We can consider a sentence valid if it conforms to the following rules:

The sentence must start with a capital letter, followed by a lowercase letter or a space.
All other characters must be lowercase letters, separators (,,;,:) or terminal marks (.,?,!,‽).
There must be a single space between each word.
The sentence must end with a terminal mark immediately following a word.
"""
from re import match

lowercase_chars_regex = '[a-z]'
seperators = [",", ":", ";"]
terminal_marks = [".", "?", "!", "‽"]

def is_valid_sentence(string):
    """Takes in a sentence and checks to see if it's valid or not"""
    is_new_sentence = True

    for i, char in enumerate(string):
        if is_new_sentence and char is not " ":
            uppercased_char = char.upper()

            if char != uppercased_char:
                return False
            else:
                is_new_sentence = False

        elif not is_new_sentence and char == " ":
            if i == len(string) - 1 and string[i - 1] == " ":
                return False
            elif string[i - 1] == " " or string[i + 1] == " ":
                return False
            elif string[i - 1] in terminal_marks:
                is_new_sentence = True
        
        elif char in terminal_marks and match(lowercase_chars_regex, string[i - 1]):
            continue

        elif match(lowercase_chars_regex, char):
            continue
            
        else:
            return False
    
    return True

