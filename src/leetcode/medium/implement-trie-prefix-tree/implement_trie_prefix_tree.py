"""
https://leetcode.com/problems/implement-trie-prefix-tree

A trie (pronounced as "try") or prefix tree is a tree data structure used to efficiently store and retrieve keys in a dataset of strings. There are various applications of this data structure, such as autocomplete and spellchecker.

Implement the Trie class:

Trie() Initializes the trie object.
void insert(String word) Inserts the string word into the trie.
boolean search(String word) Returns true if the string word is in the trie (i.e., was inserted before), and false otherwise.
boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

Example 1:
Input
["Trie", "insert", "search", "search", "startsWith", "insert", "search"]
[[], ["apple"], ["apple"], ["app"], ["app"], ["app"], ["app"]]
Output
[null, null, true, false, true, null, true]

Explanation
Trie trie = new Trie();
trie.insert("apple");
trie.search("apple");   // return True
trie.search("app");     // return False
trie.startsWith("app"); // return True
trie.insert("app");
trie.search("app");     // return True

Constraints:
1 <= word.length, prefix.length <= 2000
word and prefix consist only of lowercase English letters.
At most 3 * 104 calls in total will be made to insert, search, and startsWith.
"""

class Node:
    def __init__(self, word_totals = 0, value = None):
        self.value = value
        self.children = {}
        self.word_totals = word_totals

class Trie:
    def __init__(self):
       self.root = Node()

    def insert(self, word: str) -> None:
        current = self.root
        word_index = 0
        
        while word_index < len(word):
            if not word[word_index] in current.children:
                current.children[word[word_index]] = Node(0, word[word_index])
                
            current = current.children[word[word_index]]
            word_index += 1
        
        current.word_totals += 1

    def search(self, word: str) -> bool:
        current = self.root
        word_index = 0
        
        while word_index < len(word):
            if not word[word_index] in current.children:
                return False
            
            current = current.children[word[word_index]]
            word_index += 1
            
        return current.word_totals > 0

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        prefix_index = 0
        
        while prefix_index < len(prefix):
            if not prefix[prefix_index] in current.children:
                return False
            
            current = current.children[prefix[prefix_index]]
            prefix_index += 1
            
        stack = [current]
        
        while len(stack) > 0:
            current = stack.pop()
            
            if current.word_totals > 0:
                return True
            
            for child in current.children:
                stack.append(current.children[child])
        
        return False