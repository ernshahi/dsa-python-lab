"""
Implement Trie Methods
DESCRIPTION
Implement the search, startsWith, and delete methods of a Trie.

search(word) returns true if the word is in the Trie, and false otherwise.
startsWith(prefix) returns true if any word in the Trie starts with the given prefix, and false otherwise.
delete(word) removes the word from the Trie, and does not return a value.
The creation of the Trie and the insert method are already implemented for you.

The test cases include two parameters:

initialWords: a list of words to add to the Trie,
commands: a list of commands to run. Each command is a tuple, where the first element is "search", "startsWith", or "delete", and the second element is the word or prefix.
The test cases will create the Trie with the initial words, and then run the commands in order, and compare the output to the expected output. Note we only compare the output of search and startsWith commands, not delete commands.

Input:
initialWords = ["apple", "app", "apartment"]
commands = [
["search", "apple"],
["search", "apartment"],
["search", "appl"],
["delete", "app"],
["search", "app"],
]

Output: [True, True, False, False]

Explanation:

Trie.search("apple") -> True
Trie.search("apartment") -> True
Trie.search("appl") -> False
Trie.delete("app") -> None # Return value not checked
Trie.search("app") -> False
"""
from typing import List, Tuple

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                current_node.children[char] = TrieNode()
            current_node = current_node.children[char]
        current_node.is_end_of_word = True

    def search(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return current_node.is_end_of_word

    def delete_with_iteration(self, word:str):
        stack: List[Tuple[TrieNode, str]] = [] # (parent, char) for backtrack
        current_node = self.root

        for char in word:
            if char not in current_node.children:
                return False # no word found
            stack.append((current_node, char))
            current_node = current_node.children[char]

        if not current_node.is_end_of_word:
            return False # word not found
        current_node.is_end_of_word = False # actually deleting/removing from tree

        # prune unnecessary nodes
        for parent, char in reversed(stack):
            child = parent.children[char]
            if child.is_end_of_word or child.children:
                break
            del parent.children[char]
    
    def delete_recursion(self, word):
        def _delete(current_node: TrieNode, index: int):
            if index == len(word):
                if not current_node.is_end_of_word:
                    return False
                current_node.is_end_of_word = False # actually deleting/removing from tree
                return len(current_node.children) == 0
            
            char = word[index]
            node = current_node.children.get(char) # word may not exist in the tree
            if node is None:
                return False    
            if _delete(node, index+1):
                del current_node.children[char]
            return len(current_node.children) == 0 and not current_node.is_end_of_word
        return _delete(self.root, 0)
            
    def has_prefix(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True