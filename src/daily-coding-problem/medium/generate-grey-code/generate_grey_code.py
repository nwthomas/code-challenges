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
    final_bits = []
    initial_bits = [num_bits * 0] * (num_bits * num_bits)

    def make_new_bit(prev_bit):
        bit_str = str(prev_bit)
        new_bit = None
        initial_one = True if bit_str[0] == "1" else False

        for i in range(len(bit_str) - 1, -1):
            if initial_one and bit_str[i] == "1":
                new_bit = bit_str[:i] + "0"
                if i + 1 < len(bit_str) - 1:
                    new_bit += bit_str[i+1:]
                break
            if not initial_one and bit_str[i] == "0":
                new_bit = bit_str[:i] + "1"
                if i + 1 < len(bit_str) - 1:
                    new_bit += bit_str[i+1:]
                break

        return int(new_bit)

    for i in range(0, len(initial_bits)):
        temp_bit = None
        if i > 0:
            temp_bit = make_new_bit(initial_bits[i - 1])
        final_bits.append(temp_bit)

    return final_bits
