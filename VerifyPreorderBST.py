''' Verify Preorder Sequence in Binary Search Tree
Medium

328

37

Favorite

Share
Given an array of numbers, verify whether it is the correct preorder traversal sequence of a binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree: 

     5
    / \
   2   6
  / \
 1   3
Example 1:

Input: [5,2,6,1,3]
Output: false
Example 2:

Input: [5,2,1,3,6]
Output: true
'''

# Python program for an efficient solution to check if 
# a given array can represent Preorder traversal of 
# a Binary Search Tree 

INT_MIN = -2**32

def checkBST(pre):
    s = []
    root = INT_MIN
    for value in pre:
        if value < root:
            return False
        while len(s) > 0 and s[-1] < value:
            root = s.pop()
        s.append(value)
    return True

# Driver Program 
pre1 = [40 , 30 , 35 , 80 , 100] 
print(checkBST(pre1))
pre2 = [40 , 30 , 35 , 20 , 80 , 100] 
print(checkBST(pre2))

# This code is contributed by Nikhil Kumar Singh(nickzuck_007) 
