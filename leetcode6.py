''' Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
'''
import collections

# def groupAnagrams(strs):
#     ans = collections.defaultdict(list)
#     for s in strs:
#         ans[tuple(sorted(s))].append(s)
#     return ans.values()

# a = ["eat", "tea", "tan", "ate", "nat", "bat"]
# print(groupAnagrams(a))
# print('jgjhgh')
a = ["eat", "tea", "tan", "ate", "nat", "bat"]
dict = {}
ans = collections.defaultdict(list)
for i in range(len(a)):
    ans[tuple(sorted(a[i]))].append(a[i])
print(ans.values())