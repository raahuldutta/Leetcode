''' Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.


The above elevation map is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. Thanks Marcos for contributing this image!

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6'''

height = [0,1,0,2,1,0,1,3,2,1,2,1]
ans = 0;
size = len(height)


for i in range(1,size - 1):
    max_left = 0 
    max_right = 0
    for j in range(i,0,-1):
        max_left = max(max_left,height[j])
    for j in range(i,size):
        max_right = max(max_right, height[j])
    ans += min(max_left,max_right) - height[i]

print(ans)