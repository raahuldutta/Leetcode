''' Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
    Input: [0,1,0,3,12]
    Output: [1,3,12,0,0]
'''

a = [0,1,0,3,12]

zeroCount = 0
for i in range(len(a)):
    if a[i] == 0:
        zeroCount += 1

print(zeroCount)

for i in range()
