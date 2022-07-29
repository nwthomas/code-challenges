"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Run-length encoding is a fast and simple method of encoding strings. The basic idea is to represent repeated successive characters as a single count and character. For example, the string "AAAABBBCCDAA" would be encoded as "4A3B2C1D2A".

Implement run-length encoding and decoding. You can assume the string to be encoded have no digits and consists solely of alphabetic characters. You can assume the string to be decoded is valid.
"""

def encode_run_length(s: str) -> str:
    if type(s) != str:
        raise TypeError("Argument for encode_run_length must be of type string")

    tracker = {}
    final_chars = []

    for i, char in enumerate(s):
        if not char in tracker:
            tracker[char] = 0

        tracker[char] += 1

        if i == len(s) - 1 or char != s[i + 1]:
            number = tracker[char]
            del tracker[char]
            final_chars.extend((f"{number}", char))

    return "".join(final_chars)