# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def Traverse(self, rootNode, result, low, high):
        if rootNode is None:
            return
        if low <= rootNode.val <= high:
            result.append(rootNode.val)
        self.Traverse(rootNode.left, result, low, high)
        self.Traverse(rootNode.right, result, low, high)

    def rangeSumBST(self, root, low, high):
        result = []
        self.Traverse(root, result, low, high)
        return sum(result)
