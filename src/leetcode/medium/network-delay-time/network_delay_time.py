"""
https://leetcode.com/problems/network-delay-time

You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time it takes for a signal to travel from source to target.

We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the signal. If it is impossible for all the n nodes to receive the signal, return -1.

Example 1:
Input: times = [[2,1,1],[2,3,1],[3,4,1]], n = 4, k = 2
Output: 2

Example 2:
Input: times = [[1,2,1]], n = 2, k = 1
Output: 1

Example 3:
Input: times = [[1,2,1]], n = 2, k = 2
Output: -1
 
Constraints:
1 <= k <= n <= 100
1 <= times.length <= 6000
times[i].length == 3
1 <= ui, vi <= n
ui != vi
0 <= wi <= 100
All the pairs (ui, vi) are unique. (i.e., no multiple edges.)
"""

from collections import defaultdict, deque


def networkDelayTime(times: list[list[int]], n: int, k: int) -> int:
    # node: int -> (neighbor: int, time: int)
    nodeToNeighbors = defaultdict(set)

    for node, neighbor, time in times:
        nodeToNeighbors[node].add((neighbor, time))

    q = deque([(k, 0)])  # -> (node: int, time: int)
    seen = {k: 0}  # -> {node: time}

    while q:
        currentNode, currentTime = q.popleft()
        neighbors = nodeToNeighbors[currentNode]

        for neighbor, newTime in neighbors:
            if neighbor not in seen or (neighbor in seen and seen[neighbor] > currentTime + newTime):
                seen[neighbor] = currentTime + newTime
                q.append((neighbor, currentTime + newTime))

    if len(list(seen.keys())) == n:
        maxSeen = 0

        for time in seen.values():
            maxSeen = max(maxSeen, time)

        return maxSeen

    return -1
