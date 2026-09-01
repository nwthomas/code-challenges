"""
Shortest Word Edit Path
Given two words source and target, and a list of words words, find the length of the shortest series of edits that transforms source to target.

Each edit must change exactly one letter at a time, and each intermediate word (and the final target word) must exist in words.

If the task is impossible, return -1.

Examples:
source = "bit", target = "dog"
words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
output: 5
explanation: bit -> but -> put -> pot -> pog -> dog has 5 transitions.

source = "no", target = "go"
words = ["to"]
output: -1
"""

from collections import deque
from string import ascii_lowercase


def shortestWordEditPath(source: str, target: str, words: list[str]) -> int:
    wordSet = set(words)

    if target not in words:
        return -1

    queue = deque([(source, 0)])
    wordSet.discard(source)

    while queue:
        word, distance = queue.popleft()

        if word == target:
            return distance

        for i in range(len(word)):
            for char in ascii_lowercase:
                if char == word[i]:
                    continue

                nextWord = word[:i] + char + word[i + 1:]

                if nextWord not in wordSet:
                    continue

                wordSet.remove(nextWord)
                queue.append((nextWord, distance + 1))

    return -1
