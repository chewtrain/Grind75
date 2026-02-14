# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        return self.getheight(root)!=-1


    def getheight(self,node):
        if not node:
            return 0
        leftheight=self.getheight(node.left)
        if leftheight==-1:
            return -1
        rightheight=self.getheight(node.right)
        if rightheight==-1:
            return -1
        if abs(leftheight-rightheight)>1:
            return -1
        return max(leftheight,rightheight)+1