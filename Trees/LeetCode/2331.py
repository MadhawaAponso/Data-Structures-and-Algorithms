# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if (root.val == 0 or root.val ==1):
            return bool(root.val)
        else:
            while root is not None:
                if root.left.val == 1 or root.left.val == 0:
                    leftv = bool(root.left.val)
                else:
                    leftv = self.evaluateTree(root.left)
                if root.right.val ==1 or root.right.val == 0:
                    rightv = bool(root.right.val)
                else:
                    rightv = self.evaluateTree(root.right)
                if root.val ==2:
                    return (leftv or rightv)
                else:
                    return (leftv and rightv)
        
        