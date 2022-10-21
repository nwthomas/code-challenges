"""
Good morning! Here's your coding interview problem for today.

This question was asked by Snapchat.

Given the head to a singly linked list, where each node also has a “random” pointer that points to anywhere in the linked list, deep clone the list.
"""

class Node:
    def __init__(self, value, next_node = None, random_node = None):
        self.value = value
        self.next_node = next_node
        self.random_node = random_node

def deep_clone_random_pointer_list(l):
    stack = [l]
    cache = { l: Node(l.value) }

    while len(stack) > 0:
        current = stack.pop()
        next_node = current.next_node
        random_node = current.random_node

        new_current = cache[current]

        if next_node in cache:
            new_current.next_node = cache[next_node]
        elif next_node:
            new_next_node = Node(next_node.value)
            cache[next_node] = new_next_node
            stack.append(next_node)
            new_current.next_node = new_next_node

        if random_node in cache:
            new_current.random_node = cache[random_node]
        elif random_node:
            new_random_node = Node(random_node.value)
            cache[random_node] = new_random_node
            stack.append(random_node)
            new_current.random_node = new_random_node

    return cache[l]