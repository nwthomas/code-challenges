"""
Starting with a 1-indexed array of zeros and a list of operations, for each operation add a value to each the array element between two given indices, inclusive. Once all operations have been performed, return the maximum value in the array.

Example
n = 10
queries = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]

Queries are interpreted as follows:

    a b k
    1 5 3
    4 8 7
    6 9 1

Add the values of k between the indices a and b inclusive:

index->	 1 2 3  4  5 6 7 8 9 10
	[0,0,0, 0, 0,0,0,0,0, 0]
	[3,3,3, 3, 3,0,0,0,0, 0]
	[3,3,3,10,10,7,7,7,0, 0]
	[3,3,3,10,10,8,8,8,1, 0]

The largest value is 10 after all operations are performed.

Function Description

Complete the function arrayManipulation in the editor below.

arrayManipulation has the following parameters:

int n - the number of elements in the array
int queries[q][3] - a two dimensional array of queries where each queries[i] contains three integers, a, b, and k.

Returns

int - the maximum value in the resultant array
"""

def array_manipulation(queries):
    """Finds the largest sum of potentially overlapping summation queries on an array of length n"""
    tracker =  {}
    largest_value = 0

    for i in range(len(queries)):
        start, end, value = queries[i]

        if not start in tracker:
            tracker[start] = 0;
            
        tracker[start] += value

        if not end + 1 in tracker:
            tracker[end + 1] = 0

        tracker[end + 1] -= value;

    current_total = 0

    for key in tracker:
        current_total += tracker[key]

        if current_total > largest_value:
            largest_value = current_total

    return largest_value
