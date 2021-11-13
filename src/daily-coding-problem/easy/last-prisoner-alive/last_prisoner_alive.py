"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Bloomberg.

There are N prisoners standing in a circle, waiting to be executed. The executions are carried out starting with the kth person, and removing every successive kth person going clockwise until there is no one left.

Given N and k, write an algorithm to determine where a prisoner should stand in order to be the last survivor.

For example, if N = 5 and k = 2, the order of executions would be [2, 4, 1, 5, 3], so you should return 3.

Bonus: Find an O(log N) solution if k = 2.
"""

def get_last_alive_prisoner(n, k):
    # Create list of indices which preserves final index state
    prisoners = [i for i in range(0, n)]
    current_index = k

    while len(prisoners) > 1:
        start = prisoners[:current_index]
        end = prisoners[current_index + 1:] if current_index + 1 < len(prisoners) else []
        prisoners = start + end
        
        # Handle scenario where index is > len(list) after execution
        if current_index >= len(prisoners):
            current_index = 0
        
        # Set new current index and handle rotating around circle of prisoners
        raw_index_total = current_index + k
        current_index = raw_index_total if raw_index_total < len(prisoners) else raw_index_total % len(prisoners)

    return prisoners[0]