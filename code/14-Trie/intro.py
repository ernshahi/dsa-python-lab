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
        def _delete(current_node: TrieNode, word:str, index: int):
            if index == len(word):
                if not current_node.is_end_of_word:
                    return False
                current_node.is_end_of_word = False # actually deleting/removing from tree
                return len(current_node.children) == 0
            
            char = word[index]
            node = current_node.children.get(char)
            if node is None: 
                return False    
            
            should_delete_child = _delete(node, word, index+1)
            if should_delete_child:
                del current_node.children[char]
                return len(current_node.children) == 0 and not current_node.is_end_of_word
            return False
        return _delete(self.root, word, 0)
            
    def has_prefix(self, word):
        current_node = self.root
        for char in word:
            if char not in current_node.children:
                return False
            current_node = current_node.children[char]
        return True
        
