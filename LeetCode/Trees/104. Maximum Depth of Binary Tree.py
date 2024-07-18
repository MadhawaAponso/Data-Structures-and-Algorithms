# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxi(self,root):
        if not root:
            return 0
        else:
            l=self.maxi(root.left)
            r=self.maxi(root.right)
            return max(l,r)+1

    def maxDepth(self, root: Optional[TreeNode]) -> int:
        return self.maxi(root)
    
################################################################################################################################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #height for a node will be max(height(child1) ,height(child2)) + 1
        def getHeight(node):
            if not node: return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        return getHeight(root)
    
