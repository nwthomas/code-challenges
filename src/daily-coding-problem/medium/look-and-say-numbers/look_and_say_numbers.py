"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Epic.

The "look and say" sequence is defined as follows: beginning with the term 1, each subsequent term visually describes the digits appearing in the previous term. The first few terms are as follows:

1
11
21
1211
111221

As an example, the fourth term is 1211, since the third term consists of one 2 and one 1.

Given an integer N, print the Nth term of this sequence.
"""


def find_nth_look_and_say_number(number):
    if type(number) != int:
        raise TypeError("The argument for find_nth_look_and_say_number must be of type int.")

    final_number = "1"
    count = 1

    while count < number:
        new_final_number = ""
        current_number = final_number[0]
        count_of_current_number = 1

        for i, char in enumerate(final_number):
            if i > 0:
                if char != current_number:
                    new_final_number += f"{count_of_current_number}{current_number}"
                    current_number = char
                    count_of_current_number = 1
                else:
                    count_of_current_number += 1

        if i == len(final_number) - 1:
            new_final_number += f"{count_of_current_number}{current_number}"

        final_number = new_final_number
        count += 1
    
    return int(final_number)

