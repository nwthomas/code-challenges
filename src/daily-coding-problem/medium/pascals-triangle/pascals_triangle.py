"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stitch Fix.

Pascal's triangle is a triangular array of integers constructed with the following formula:

The first row consists of the number 1.
For each subsequent row, each element is the sum of the numbers directly above it, on either side.
For example, here are the first few rows:

    1
   1 1
  1 2 1
 1 3 3 1
1 4 6 4 1
Given an input k, return the kth row of Pascal's triangle.

Bonus: Can you do this using only O(k) space?
"""


def find_pascals_triangle_row(k):
    if type(k) is not int:
        raise TypeError(
            "The argument for find_pascals_triangle_row must be of type int.")

    elif k <= 0:
        return None

    elif k == 1:
        return [1]

    elif k == 2:
        return [1, 1]

    else:
        row_number = 3
        row = [1, 2, 1]

        while row_number < k:
            old_row_length = len(row)
            index = 0
            previous = 1

            while index < old_row_length + 1:
                if index == old_row_length:
                    row.append(1)

                elif index > 0:
                    new_value = previous + row[index]
                    previous = row[index]
                    row[index] = new_value

                index += 1

            row_number += 1

        return row
