''' Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
'''
# from collections import Counter
# nums = [0,1,0,3,12]

# dict = Counter(nums)
# nums = list(dict.keys())[1:]
# for i in range(dict[0]):
#     nums.append(0)
# print(nums)

i = 0
nums = [0,1,0,3,12]
for j in range(len(nums)):
    if nums[j] != 0:
        nums[i], nums[j] = nums[j],nums[i]
        i = i+ 1
print(nums)