"""
127. Word Ladder

A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

Every adjacent pair of words differs by a single letter.
Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
sk == endWord
Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.

 

Example 1:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
Output: 5
Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

Example 2:
Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
Output: 0
Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
 

Constraints:

1 <= beginWord.length <= 10
endWord.length == beginWord.length
1 <= wordList.length <= 5000
wordList[i].length == beginWord.length
beginWord, endWord, and wordList[i] consist of lowercase English letters.
beginWord != endWord
All the words in wordList are unique.

"""
from typing import List
from collections import defaultdict, deque

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time Complexity: O(N * L²) # N-number of words in the wordList, L-length of the words
        Space Complexity: O(N * L²) # N-number of words in the wordList, L-length of the words
        """
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj_list = defaultdict(list)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                adj_list[pattern].append(word)

        queue = deque([beginWord])
        visited = set([beginWord])
        result = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for nei in adj_list[pattern]:
                        if nei not in visited:
                            queue.append(nei)
                            visited.add(nei)
            result += 1
        return 0

    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        """
        Time Complexity: O(n^2 * k) # n-number of words in the wordList, k - length of the words
        Space Complexity: O(n^2) # n-number of words in the wordList, n^2 - adjacency list
        """
        if endWord not in wordList:
            return 0
        wordList.append(beginWord)
        adj_list = defaultdict(list)
        for i in range(len(wordList)):
            curr_word = wordList[i]
            for j in range(i+1, len(wordList)):
                word = wordList[j]
                diff = sum(c1 != c2 for c1, c2 in zip(word, curr_word))
                if diff <= 1:
                    adj_list[curr_word].append(word)
                    adj_list[word].append(curr_word)
        queue = deque([beginWord])
        visited = set([beginWord])
        result = 1
        while queue:
            for i in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return result
                for nei in adj_list[word]:
                    if nei not in visited:
                        queue.append(nei)
                        visited.add(nei)
            result += 1
        return 0
