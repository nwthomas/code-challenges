"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Apple.

Gray code is a binary code where each successive value differ in only one bit, as well as when wrapping around. Gray code is common in hardware so that we don't see temporary spurious values during transitions.

Given a number of bits n, generate a possible gray code for it.

For example, for n = 2, one gray code would be [00, 01, 11, 10].
"""


def find_grey_code_bits(num_bits):
    """
    Takes in the number of bits and returns a list of unique grey code combinations
    """
    if type(num_bits) is not int:
        return None
    if num_bits <= 0:
        return []

    final_bits = []
    initial_bit = "0" * num_bits
    length = 2 if num_bits is 1 else num_bits * num_bits

    def make_new_bit(bit_str):
        new_bit = bit_str
        initial_one = True if bit_str[0] == "1" else False

        for i in range(len(bit_str) - 1, -1, -1):
            if initial_one and bit_str[i] == "1":
                new_bit = bit_str[:i] + "0"
                if i + 1 < len(bit_str):
                    new_bit += bit_str[i+1:]
                break
            if not initial_one and bit_str[i] == "0":
                new_bit = bit_str[:i] + "1"
                if i + 1 < len(bit_str):
                    new_bit += bit_str[i+1:]
                break
        return new_bit

    for i in range(0, length):
        temp_bit = initial_bit if i == 0 else final_bits[i - 1]
        if i > 0:
            temp_bit = make_new_bit(temp_bit)
        if i > 0 and temp_bit == initial_bit:
            break
        final_bits.append(temp_bit)

    return final_bits
