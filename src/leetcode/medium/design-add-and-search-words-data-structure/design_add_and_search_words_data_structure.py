"""
https://leetcode.com/problems/design-add-and-search-words-data-structure

Design a data structure that supports adding new words and finding if a string matches any previously added string.

Implement the WordDictionary class:

WordDictionary() Initializes the object.
void addWord(word) Adds word to the data structure, it can be matched later.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example:
Input
["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
[[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
Output
[null,null,null,null,false,true,true,true]

Explanation
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("bad");
wordDictionary.addWord("dad");
wordDictionary.addWord("mad");
wordDictionary.search("pad"); // return False
wordDictionary.search("bad"); // return True
wordDictionary.search(".ad"); // return True
wordDictionary.search("b.."); // return True

Constraints:
1 <= word.length <= 25
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 3 dots in word for search queries.
At most 104 calls will be made to addWord and search.
"""

class Node:
    def __init__(self, word_totals: int = 0, value = None):
        self.value = value
        self.children = {}
        self.word_totals = word_totals

class WordDictionary:
    def __init__(self):
        self.root = Node()
        

    def addWord(self, word: str) -> None:
        current = self.root
        word_index = 0
        
        while word_index < len(word):
            if not word[word_index] in current.children:
                current.children[word[word_index]] = Node(0, word[word_index])
                
            current = current.children[word[word_index]]
            word_index += 1
            
        current.word_totals += 1

    def search(self, word: str) -> bool:
        def dfs(j, root):
            cur = root
            
            for i in range(j, len(word)):
                c = word[i]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if c not in cur.children:
                        return False
                    cur = cur.children[c]
            return cur.word_totals > 0
        
        return dfs(0, self.root)