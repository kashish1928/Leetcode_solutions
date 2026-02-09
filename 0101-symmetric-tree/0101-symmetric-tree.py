# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.isSame(root.left,root.right)
    
    def isSame(self,left: Optional[TreeNode],right: Optional[TreeNode]) -> bool:
        if(left is None):
            return (right is None)
        if(right is None):
            return False
        if(left.val == right.val):
            return self.isSame(left.left,right.right) and self.isSame(right.left,left.right)
        else:
            return False