''' Permutations
Medium

1829

55

Favorite

Share
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output:
[
  [1,2,3],
  [1,3,2],
  [2,1,3],
  [2,3,1],
  [3,1,2],
  [3,2,1]
]'''

def backtrack(first = 0):
    if first == n:  
        output.append(nums[:])
    for i in range(first, n):
        nums[first], nums[i] = nums[i], nums[first]
        backtrack(first + 1)
        nums[first], nums[i] = nums[i], nums[first]
nums = [1,2,3]      
n = len(nums)
output = []
backtrack()
print(output)