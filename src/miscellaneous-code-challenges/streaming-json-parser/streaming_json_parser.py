"""
A language model streams its output as JSON, and the client wants to show what has arrived so far without waiting for the stream to finish. Given the text received so far, which may stop at any character, return the value it represents with everything still unfinished closed off. The JSON contains only strings and arrays that can be nested; there are no objects, numbers, booleans or nulls.

The text can stop partway through a string, which keeps only the characters received so far. It can stop while arrays are still open, and it can stop right after a comma. In the interview you also wrote your own tests for the function, so plan the cases you would check.

Function Signature

Rules
- text is a prefix of a valid JSON value built only from strings and arrays, possibly the whole value. It can end anywhere: inside a string, right after an opening quote, right after [ , right after a comma, or in the spaces between tokens.
- Return each array as a Python list and each string as a Python str , in the order they appear.
- A string whose opening quote has arrived is part of the result, holding the characters received so far. If none have arrived yet, it is the empty string "" .
- A comma with no value after it yet adds nothing to its array.
- Every array that has been opened but not yet closed is closed in the result.
- The top-level value can itself be a string: '"hel' returns "hel" .
- If text is a complete value, return that value unchanged.

Constraints
1 <= len(text) <= 10^5
text[0] is [ or " .
"""


def parse_streaming_json(s):
    i = 0

    def parse():
        nonlocal i

        while i < len(s) and s[i].isspace():
            i += 1

        if i >= len(s):
            return None

        # String
        if s[i] == '"':
            i += 1
            start = i

            while i < len(s) and s[i] != '"':
                i += 1

            result = s[start:i]

            if i < len(s):
                i += 1  # Closing quote

            return result

        # Array
        if s[i] == '[':
            i += 1
            result = []

            while i < len(s):
                while i < len(s) and (s[i].isspace() or s[i] == ','):
                    i += 1

                if i >= len(s) or s[i] == ']':
                    if i < len(s):
                        i += 1
                    break

                value = parse()

                if value is None:
                    break

                result.append(value)

            return result

        return None

    return parse()
