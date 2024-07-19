# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
 
    
################################################################################################################################
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #height for a node will be max(height(child1) ,height(child2)) + 1
        def getHeight(node):
            if not node: return 0
            return max(getHeight(node.left), getHeight(node.right)) + 1
        
        return getHeight(root)
    
