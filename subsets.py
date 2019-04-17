''' Given a set of distinct integers, nums, return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.

Example:

Input: nums = [1,2,3]
Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]'''
nums = [1,2,3]
res = []
for i in range(pow(2,len(nums))):
    tmp=[]
    for j in range(len(nums)):
        if i&1:
            tmp.append(nums[j])
        i>>=1
    res.append(tmp)
print(res)
    