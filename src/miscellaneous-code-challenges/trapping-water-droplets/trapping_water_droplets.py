"""
Your goal is to trap water droplets inside a 2D matrix.

In this matrix, "W" represents a wall, and "E" represents an empty space. Here is an example:

[
    ["E", "W", "E", "W", "E", "W"],
    ["E", "W", "E", "W", "E", "W"],
    ["E", "W", "E", "W", "E", "W"],
]

In the above example, the walls would trap 6 water droplets. This is because the left-most column does not have a wall to confine water droplets.

Here is another example:

[
    ["E", "E", "E", "W", "E", "W"],
    ["E", "W", "E", "W", "E", "W"],
    ["E", "W", "E", "W", "E", "W"],
]

In that example, the walls would trap 5 water droplets. This is because the left-most wall only extends to a height of 2.

Please write an altorithm that finds the number of water droplets that would be trapped in a given matrix.
"""

from typing import List

def trap_water_droplets(matrix: List[List[str]]) -> int:
    # DP matrix for calculating droplets trapped
    tracker = [[0 for _ in range(len(matrix[0]))] for _ in range(len(matrix))]

    # While not used later, this is set early so that it can be used in edge cases inside loops
    count = 0;

    for i in range(0, len(matrix), 1):
        # Set pointers
        left = 0
        right = len(matrix[i]) - 1;

        # Set boolean flags for tracking presence of walls
        has_found_left_wall = False
        has_found_right_wall = False

        while left <= right:
            # Check for walls
            if matrix[i][left] == "W":
                has_found_left_wall = True
            if matrix[i][right] == "W":
                has_found_right_wall = True

            # If we haven't found both walls, gradually increment and continue
            if not has_found_left_wall:
                left += 1
                continue
            if not has_found_right_wall:
                right -= 1
                continue

            # If this point is reached, both walls have been found and droplets can be counted
            if matrix[i][left] == "E":
                tracker[i][left] += 1

                if i - 1 >= 0:
                    tracker[i][left] += tracker[i - 1][left]
            if left != right and matrix[i][right] == "E":
                tracker[i][right] += 1

                if i - 1 >= 0:
                    tracker[i][right] += tracker[i - 1][right]

            # Check for presence of short wall with droplets trapped above it with suroounding walls.
            # In this instance, pre-count droplets as this is a dead end for this dp column.
            if matrix[i][left] == "W" and i - 1 >= 0 and tracker[i - 1][left] > 0:
                count += tracker[i - 1][left]
            if left != right and matrix[i][right] == "W" and i - 1 >= 0 and tracker[i - 1][right] > 0:
                count += tracker[i - 1][right]

            # Update pointers concurrently for next iteration
            left += 1
            right -= 1

    # Sum up the total droplets trapped from the last row (not counting short walls inside larger
    # containments that were added earlier in the algorithm)
    for num in tracker[len(matrix) - 1]:
        count += num

    return count