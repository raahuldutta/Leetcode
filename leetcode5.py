''' Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Example:

Input: [0,1,0,3,12]
Output: [1,3,12,0,0
'''

a = [0,1,0,3,12]
zerocount = 0
b = []
for i in range(len(a)):
    if a[i] == 0:
        zerocount += 1
    else:
        b.append(a[i])

for i in range(zerocount):
    b.append(0)
print(b)
