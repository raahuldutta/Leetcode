''' Given a non-empty string s and a dictionary wordDict containing a list of non-empty words, determine if s can be segmented into a space-separated sequence of one or more dictionary words.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.
Example 1:

Input: s = "leetcode", wordDict = ["leet", "code"]
Output: true
Explanation: Return true because "leetcode" can be segmented as "leet code".
Example 2:

Input: s = "applepenapple", wordDict = ["apple", "pen"]
Output: true
Explanation: Return true because "applepenapple" can be segmented as "apple pen apple".
             Note that you are allowed to reuse a dictionary word.
Example 3:

Input: s = "catsandog", wordDict = ["cats", "dog", "sand", "and", "cat"]
Output: false
'''
s = "applepenapple"
wordDict = ["apple", "pen"]

# for i in range(len(s)):
#     if s[:i] in wordDict and s[i:] in wordDict:
#         print(s[:i])
#         print(s[i:])

def word_Break(self, s, wordDict, start):
    if (start == len(s)):
            return True
    for end in range(start+1, len(s)):
        if s[start: end] in wordDict:
            if self.word_Break(s[end:], wordDict, 0):
                return True
    return False

s = "applepenapple"
wordDict = ["apple", "pen"]
if self.word_Break(s,wordDict,0):
    print('fouind')