"""
Write an efficient function that checks whether any permutation of an input string is a palindrome.

You can assume the input string only contains lowercase letters.

Examples:

"civic" should return True
"ivicc" should return True
"civil" should return False
"livci" should return False
"But 'ivicc' isn't a palindrome!"

If you had this thought, read the question again carefully. We're asking if any permutation of the string is a palindrome. Spend some extra time ensuring you fully understand the question before starting. Jumping in with a flawed understanding of the problem doesn't look good in an interview.
"""


def is_permutation_palindrome(string):
    """Returns True if a permutation is a variation of a palindrome or False otherwise"""

    if type(string) != str:
        raise TypeError(
            "The argument for is_permutation_palindrome must be of type string.")

    tracker = set()

    for char in string:
        if char in tracker:
            tracker.remove(char)
        else:
            tracker.add(char)

    return len(tracker) <= 1
