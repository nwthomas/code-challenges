"""
You are given q queries. Each query is of the form two integers described below:
- 1:x Insert x in your data structure.
- 2:y Delete one occurence of y from your data structure, if present.
- 3:z Check if any integer is present whose frequency is exactly . If yes, print 1 else 0.

The queries are given in the form of a 2-D array  of size  where  contains the operation, and  contains the data element.

Example
queries = [(1, 1), (2, 2), (3, 2), (1, 1), (1, 1), (2, 1), (3, 2)]

The results of each operation are:

Operation   Array   Output
(1,1)       [1]
(2,2)       [1]
(3,2)                   0
(1,1)       [1,1]
(1,1)       [1,1,1]
(2,1)       [1,1]
(3,2)                   1

Return an array with the output: [0, 1].

Function Description

Complete the freqQuery function in the editor below.

freqQuery has the following parameter(s):

- int queries[q][2]: a 2-d array of integers

Returns

- int[]: the results of queries of type 3
"""

def freqQuery(queries):
    valueToCount = {}
    countToValue = {}
    printQueries = []
    
    for query in queries:
        operation, value = query
        
        if operation == 1 and not value in valueToCount:
            valueToCount[value] = 1
            
            if not 1 in countToValue:
                countToValue[1] = {}
            
            countToValue[1][value] = True
            
        elif operation == 1:
            previousCount = valueToCount[value]
            nextCount = previousCount + 1
            valueToCount[value] = nextCount
            
            del countToValue[previousCount][value]
            
            if not nextCount in countToValue:
                countToValue[nextCount] = {}
                
            countToValue[nextCount][value] = True
            
        elif operation == 2 and value in valueToCount and valueToCount[value] > 0:
            previousCount = valueToCount[value]
            nextCount = valueToCount[value] - 1
            valueToCount[value] = nextCount
            
            del countToValue[previousCount][value]
            
            if nextCount == 0:
                del valueToCount[value]
            else:
                countToValue[nextCount][value] = True
            
        elif operation == 3 and value in countToValue and len(countToValue[value].keys()) > 0:
            printQueries.append(1)
            
        elif operation == 3:
            printQueries.append(0)

    return printQueries