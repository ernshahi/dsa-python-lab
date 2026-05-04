"""
139. Word Break

You are provided with a string s and a set of words called wordDict. Write a function to determine whether s can be broken down into a sequence of one or more words from wordDict, where each word can appear more than once and there are no spaces in s. If s can be segmented in such a way, return true; otherwise, return false.

Input:
s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output:
false
Explanation: There is no valid segmentation of "catsandog" into dictionary words from wordDict.

Input:
s = "hellointerview", wordDict = ["hello","interview"]
Output:
true
Explanation: Return true because "hellointerview" can be segmented as "hello" and "interview".
Note that you are allowed to reuse a dictionary word.
"""

def wordBreak(s, wordDict):
    dp = [False] * (len(s) + 1)
    dp[0] = True

    for i in range(1, len(s) + 1):
        for word in wordDict:
            l = len(word)
            if i >= l and dp[i - l] and s[i-l:i] == word:
                dp[i] = True
                break
    return dp[-1]