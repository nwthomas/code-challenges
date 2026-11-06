"""
https://neetcode.io/problems/count-connected-components/question

You have an undirected graph of n nodes labeled from 0 to n - 1. You are given an integer n and an array edges where edges[i] = [aᵢ, bᵢ] indicates that there is an edge between aᵢ and bᵢ in the graph.

Return the number of connected components in the graph.

Example 1:
Input:
n = 5, edges = [[0,1],[1,2],[3,4]]
Output: 2

Example 2:
Input:
n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
Output: 1

Constraints:
1 <= n <= 2000
1 <= edges.length <= 5000
edges[i].length == 2
0 <= aᵢ < n
0 <= bᵢ < n
aᵢ != bᵢ
There are no repeated edges.
"""


def countComponents(n: int, edges: list[list[int]]) -> int:
    nodeToNeighbors = {}

    for one, two in edges:
        if one not in nodeToNeighbors:
            nodeToNeighbors[one] = set()
        if two not in nodeToNeighbors:
            nodeToNeighbors[two] = set()

        nodeToNeighbors[one].add(two)
        nodeToNeighbors[two].add(one)

    for i in range(n):
        if i not in nodeToNeighbors:
            nodeToNeighbors[i] = set()

    def dfs(node: int, seen: set):
        seen.add(node)

        neighbors = nodeToNeighbors[node]
        for n in neighbors:
            if n not in seen and n in nodeToNeighbors:
                dfs(n, seen)

        del nodeToNeighbors[node]

    components = 0
    for i in range(n):
        if i in nodeToNeighbors:
            dfs(i, set())
            components += 1

        if len(nodeToNeighbors.keys()) == 0:
            break

    return components
