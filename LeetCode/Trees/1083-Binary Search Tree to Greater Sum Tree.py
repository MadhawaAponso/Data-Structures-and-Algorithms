# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def traverse(self,node,l = []):
        if not node:
            return
        self.traverse(node.left,l)
        l.append(node.val)
        self.traverse(node.right,l)
        return l
    def inorderTraverse(self,rootNode,l):
        if not rootNode:
            return
        self.inorderTraverse(rootNode.left,l)
        data = l.pop(0)
        rootNode.val = data
        self.inorderTraverse(rootNode.right,l)
        


    def bstToGst(self, root: TreeNode) -> TreeNode:
        l = self.traverse(root)
        for i in range(len(l)):
            l[i] = sum(l[i:])
        self.inorderTraverse(root,l)
        return root
        
#Time and space complexity : O(N)