/*
https://leetcode.com/problems/design-add-and-search-words-data-structure

Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

void addWord(word) Adds word to the data structure.
bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

Example 1:
Input:
["WordDictionary", "addWord", "day", "addWord", "bay", "addWord", "may", "search", "say", "search", "day", "search", ".ay", "search", "b.."]
Output:
[null, null, null, null, false, true, true, true]

Explanation:
WordDictionary wordDictionary = new WordDictionary();
wordDictionary.addWord("day");
wordDictionary.addWord("bay");
wordDictionary.addWord("may");
wordDictionary.search("say"); // return false
wordDictionary.search("day"); // return true
wordDictionary.search(".ay"); // return true
wordDictionary.search("b.."); // return true

Constraints:
1 <= word.length <= 20
word in addWord consists of lowercase English letters.
word in search consist of '.' or lowercase English letters.
There will be at most 2 dots in word for search queries.
At most 10,000 calls will be made to addWord and search.
*/

class TrieNode {
    constructor(val) {
        this.val = val;
        this.isWord = false;
        this.children = {};
    }

    setAsWord() {
        this.isWord = true;
    }

    setChild(node) {
        this.children[node.val] = node;
    }

    getChild(val) {
        return this.children[val];
    }

    getChildren() {
        return this.children;
    }
}

class WordDictionary {
    constructor() {
        this.root = new TrieNode("__root__");
    }

    /**
     * @param {string} word
     * @return {void}
     */
    addWord(word) {
        let currentNode = this.root;
        for (let i = 0; i < word.length; i++) {
            const char = word[i];

            if (!currentNode.getChild(char)) {
                currentNode.setChild(new TrieNode(char));
            }
            currentNode = currentNode.getChild(char);

            if (i === word.length - 1) {
                currentNode.setAsWord();
            }
        }
    }

    /**
     * @param {string} word
     * @return {boolean}
     */
    search(word) {
        function bfs(node, i) {
            if (i === word.length && node.isWord) {
                return true;
            }

            const nodeChildren = node.getChildren();
            if (!Object.keys(nodeChildren).length) {
                return false;
            }

            const char = word[i];
            const results = [];
            if (char === ".") {
                for (const child of Object.keys(nodeChildren)) {
                    results.push(bfs(nodeChildren[child], i + 1));
                }
            } else if (nodeChildren[char]) {
                results.push(bfs(nodeChildren[char], i + 1));
            }

            return results.some((result) => result);
        }

        return bfs(this.root, 0);
    }
}

module.exports = { TrieNode, WordDictionary };
