''' Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.'''

matrix = [
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
target = 5

def binary_search(matrix, target, start, vertical):
    low = start
    high = len(matrix[0])-1 if vertical else len(matrix)-1
    while high >= low:
        mid = (low + high) // 2 
        if vertical:
            if matrix[start][mid] < target:
                low = mid + 1
            elif matrix[start][mid] > target:
                high = mid - 1
            else:
                True
        else: # searching a row
                if matrix[mid][start] < target:
                    lo = mid + 1
                elif matrix[mid][start] > target:
                    hi = mid - 1
                else:
                    return True
        
        return False
for i in range(min(len(matrix), len(matrix[0]))):
    verticle_found = binary_search(matrix, target, i, True)
    horizontal_found = binary_search(matrix, target, i, False)
    if verticle_found or horizontal_found:
        print('FOund')
