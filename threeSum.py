''' Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0? Find all unique triplets in the array which gives the sum of zero.

Note:

The solution set must not contain duplicate triplets.

Example:

Given array nums = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]
'''
nums = [-1, 0, 1, 2, -1, -4]
nums.sort()
ans = []
for i in range(0,len(nums)-2):
    if nums[i]>0:
        break
    if i>0 and nums[i]==nums[i-1]:
        continue 
    p1 = i + 1
    p2 = len(nums) - 1
    p0 = nums[i]

    while(p1 < p2):
        if nums[i] + nums[p1] + nums[p2] == 0:
            newArray = []
            newArray.append(nums[i])
            newArray.append(nums[p1])
            newArray.append(nums[p2])
            ans.append(newArray)
            p1 += 1
            p2 -= 1
        elif nums[i] + nums[p1] + nums[p2] < 0:
            p1 += 1
        else:
            p2 -= 1

print(ans)
# Function to find duplicate rows in a binary matrix 
from collections import Counter 
ans2 = []
def duplicate(input): 
	input = map(tuple,input) 
	freqDict = Counter(input) 
	for (row,freq) in freqDict.items(): 
		if freq>1: 
			print(row)
        



