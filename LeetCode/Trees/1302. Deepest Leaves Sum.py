# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxdepth(self, node):
        if not node:
            return 0
        else:
            l_depth = self.maxdepth(node.left)
            r_depth = self.maxdepth(node.right)
            return max(l_depth, r_depth) + 1

    def sumOfDeepestNode(self,root,current_depth,maxdepth):
        if not root:
            return 0
        else:
            if current_depth == maxdepth:
                return root.val
            return self.sumOfDeepestNode(root.left,current_depth+1,maxdepth)+self.sumOfDeepestNode(root.right,current_depth+1,maxdepth)
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        max_depth = self.maxdepth(root)
        return self.sumOfDeepestNode(root,1,max_depth)
        
    
    
###########################################################################################################################
##Timewise best sol
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        prev = deque([root])
        
        while queue:
            prev.clear()
            prev = queue
            queue = deque([])
            
            for node in prev:
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                    
        s = 0
        for node in prev:
            s += node.val
            
        return s
    
################SPACE WISE BEST SOLUTION#############################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        
        s = [0]
        maxDepth = [0]
        def dfs(root: Optional[TreeNode], depth: int, s: List[int], maxDepth: List[int]) -> None:
            if not root:
                return
            
            if maxDepth[0] < depth:
                s[0] = root.val
                maxDepth[0] = depth
            elif maxDepth[0] == depth:
                s[0] += root.val

            dfs(root.left, depth + 1, s, maxDepth)
            dfs(root.right, depth + 1, s, maxDepth)
        
        dfs(root, 0, s, maxDepth)
        return s[0]