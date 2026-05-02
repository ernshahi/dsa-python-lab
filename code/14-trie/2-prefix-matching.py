"""
DESCRIPTION
Use a Trie to implement a prefix matching function.

match(prefix) returns a list of all words in the Trie that start with the given prefix. The words can be in any order.
The creation of the Trie is already implemented for you.

The test cases include two parameters:

words: a list of words to add to the Trie,
prefix: a prefix to search for.
The test cases will create the Trie with the initial words, and then run the match command, and compare the output to the expected output.

Example 1:

Input:

initialWords = ["apple", "app", "apartment", "ap", "apricot"]
prefix = "app"
Output: ["apple", "app"]

Example 2:

Input:

initialWords = ["ball", "bath", "bat", "batter"]
prefix = "bat"
Output: ["bat", "bath", "batter"]
"""

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Solution:
    def create_trie(self, words):
        # === DO NOT MODIFY ===
        self.root = TrieNode()
        for word in words:
            self.insert(word)

    def insert(self, word):
        # === DO NOT MODIFY ===
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.isEndOfWord = True
    
    def prefix(self, word):
        """
        Return a list of all words in the trie that start with the given prefix.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return []
            node = node.children[char]

        result = []
        def dfs(curr_node, curr_word):
            if curr_node.isEndOfWord:
                result.append(curr_word)
            for char, child_node in curr_node.children.items():
                dfs(child_node, curr_word+char)
        dfs(node, word)
        return result

    def trie(self, words, prefix):
        # === DO NOT MODIFY ===
        self.create_trie(words)
        return self.prefix(prefix)