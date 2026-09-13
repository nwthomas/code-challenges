"""
Determine if two sentences are similar. Two sentences are similar if they have the same length and each pair of corresponding words in the two sentences is similar. The similarity between words is defined by the provided list of similar word pairs. A word is always similar to itself.

For example, if we have the list of similar word pairs as [("great", "good"), ("acting", "drama"), ("skills", "talent")] , then the sentences "You have great acting skills" and "You have good drama talent" are similar.

Examples:
sentencel = ["Let's", "code", "in", "Python"]
sentence2 = ["Let's", "program", "in", "Python"]
similarPairs = [
("code", "program"'),
output: true

sentencel = ['I", "love", "to", "play", "football"]
sentence2 = ["I", "love", "playing", "soccer"]
similarPairs = [("play", "playing"), ("football", "soccer")]
output: false, different sentence lengths

sentencel = ["Do", "you", "Like", "coffee"] |
sentence = ["Do", "you", "love", "coffee"]
similarPairs = [
("like", "enjoy"), ("coffee", "tea"),
output: false, "like" is not similar to "love" based on the given pairs
"""

from collections import defaultdict


def areSentencesSimilar(sentence1: list[str], sentence2: list[str], similarPairs: list[list[str]]) -> bool:
    if len(sentence1) != len(sentence2):
        return False

    # Prep dict with adjacency lists
    similar = defaultdict(list)
    for pair in similarPairs:
        word1, word2 = pair

        if not word1 in similar:
            similar[word1] = []
        if not word2 in similar:
            similar[word2] = []

        similar[word1].append(word2)
        similar[word2].append(word1)

    # DFS traversal function
    def traverse(word1: str, word2: str, seen: set) -> bool:
        results = []

        seen.add(word1)

        for w in similar[word1]:
            if w == word2:
                return True
            if w not in seen:
                results.append(traverse(w, word2, seen))

        for r in results:
            if r:
                return True

        return False

    # Iterate through sentences and traverse with BFS to compare words
    for i in range(len(sentence1)):
        if sentence1[i] != sentence2[i]:
            if traverse(sentence1[i], sentence2[i], set()):
                continue
            else:
                return False

    return True
