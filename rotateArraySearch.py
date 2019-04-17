
def find_rotate_index(left, right):
    if nums[left] < nums[right]:
        return 0
            
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] > nums[pivot + 1]:
            return pivot + 1
        else:
            if nums[pivot] < nums[left]:
                right = pivot - 1
            else:
                left = pivot + 1
                
def search(left, right):
    while left <= right:
        pivot = (left + right) // 2
        if nums[pivot] == target:
            return pivot
        else:
            if target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
    return -1
nums = [4,5,6,7,0,1,2]        
n = len(nums)
target = 1
        
rotate_index = find_rotate_index(0, n - 1)





