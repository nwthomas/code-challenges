"""
We're building a new social network where users are friends with one another. In order to make better friend recommendations, we want to develop a "friend distance" algorithm.

Write a function friend_distance(friends, userA, userB) that returns the minimum distance between two users (similar to the "degree" of connection on LinkedIn).

The input to your function will be a 2D array friends, where each entry (A, B) contains the friendship status between user A and user B.

In the friends array, each user's friendships are represented by rows, and each column represents a user. For example, if friends[0][1] is 1, it means that user 0 is friends with user 1. Similarly, if friends[1][2] is 1, it indicates that user 1 is friends with user 2.

```
def friend_distance(friends, userA, userB):
  # Your code here...
```

Examples
In this example, users 0 and 1 are friends, so the entries (0, 1) and (1, 0) are both 1. Users 1 and 2 are also friends, so entries (1, 2) and (2, 1) are also 1. Since they are direct friends, their friend distance is 1. Users 0 and 2 are not friends but are both connected to User 1, so their friend distance is 2.

```
friends = [[0 1 0],
           [1 0 1],
           [0 1 0]]

friend_distance(friends, 0, 1) # => 1
friend_distance(friends, 1, 2) # => 1
friend_distance(friends, 0, 2) # => 2
```

Return -1 if there are no connections between the users.
"""


from collections import deque


def friend_distance(friends: list[list[int]], userA: int, userB: int) -> int:
    q = deque([(userA, 0)])
    visited = set()
    visited.add(userA)

    while q:
        current_node, current_degrees = q.popleft()
        neighbors = friends[current_node]  # something like this: [0, 1, 0]

        for i, value in enumerate(neighbors):
            if i == userB and value == 1:
                return current_degrees + 1

            if i not in visited and value == 1:
                visited.add(i)
                q.append((i, current_degrees + 1))

    return -1
