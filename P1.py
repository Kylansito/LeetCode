#Given the root of a binary tree, return its maximum depth.

class TreeNode:
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

class Solution:
    def maxDepth(self, root) -> int:
        a = b = 0
        if(not root):
            return 0
        if(root.left):
            a = self.maxDepth(root.left)
        if(root.right):
            b = self.maxDepth(root.right)
        
        return 1 + max(a, b)