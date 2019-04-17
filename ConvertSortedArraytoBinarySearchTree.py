''' Convert Sorted Array to Binary Search Tree
Easy

1046

104

Favorite

Share
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example:

Given the sorted array: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5], which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5'''
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

nums = [-10,-3,0,5,9]

def sortedArrayToBST(nums):
    if len(nums) == 0:
        return None
    else:
        mid = int(len(nums) / 2)
        root = TreeNode(nums[mid])
        root.left = sortedArrayToBST(nums[:mid])
        root.right = sortedArrayToBST(nums[mid+ 1:])
        return root

def preOrder(root):
    if root is None:
        return
    print(root.val)
    preOrder(root.left)
    preOrder(root.right)

root = sortedArrayToBST(nums)
preOrder(root)
