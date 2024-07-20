# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        def get_sumOf(root,l):
            if not root:
                return 
            else:
                if root.val%2==0:
                    if root.left :
                        if root.left.left:
                            l.append(root.left.left.val)
                        if root.left.right :
                            l.append(root.left.right.val)
                    if root.right:
                        if root.right.left:
                            l.append(root.right.left.val)
                        if root.right.right:
                            l.append(root.right.right.val)
                get_sumOf(root.left,l)
                get_sumOf(root.right,l)
            return l
        l = []
        return sum(get_sumOf(root,l))
        
#############################################################################################################################
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ans=0
        def dfs(root,p,isE):
            nonlocal ans
            if not root:
                return
            
            if isE:
                ans+=root.val

            isE=False
            if p%2==0:
                isE=True

            
            dfs(root.left,root.val,isE)
            dfs(root.right,root.val,isE)

        dfs(root,1,False)
        return ans