# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> Optional[TreeNode]:
        if not nums:
            return None
        max_val = max(nums)
        rootNode=TreeNode(max_val)
        max_index = nums.index(max_val)
        rootNode.left = self.constructMaximumBinaryTree(nums[:max_index])
        rootNode.right=self.constructMaximumBinaryTree(nums[max_index + 1:])

        return rootNode