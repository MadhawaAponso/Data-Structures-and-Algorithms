# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def depthSearch(self, root: Optional[TreeNode], s: str = "", l: List[str] = None) -> List[str]:
        if l is None:
            l = []
        
        if not root:
            return l
        
        s = s + str(root.val)
        if root.left is None and root.right is None:
            l.append(s)
        else:
            self.depthSearch(root.left, s, l)
            self.depthSearch(root.right, s, l)
        
        return l

    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        paths = self.depthSearch(root)
        total_sum = sum(int(path, 2) for path in paths)  # Convert binary strings to integers and sum them
        print(paths)
        return total_sum

####################################################################################################################
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        
        total = 0
        
        def dfs(node, path):
            nonlocal total
            if not node:
                return
            
            path.append(str(node.val))
            
            if not node.left and not node.right:
                binary_str = "".join(path)
                
                total += int(binary_str, 2)
                
                return
            if node.left:
                dfs(node.left, path)
                path.pop()
            if node.right:
                dfs(node.right, path)
                path.pop()
        
        
        dfs(root, [])
        return total