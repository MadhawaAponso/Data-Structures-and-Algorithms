# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def find_path(self, root, value, path):
        if not root:
            return False
        if root.val == value:
            return True
        path.append('L')
        if self.find_path(root.left, value, path):
            return True
        path.pop()
        
        path.append('R')
        if self.find_path(root.right, value, path):
            return True
        path.pop()
        
        return False

    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        start_path = []
        dest_path = []

        self.find_path(root, startValue, start_path)
        self.find_path(root, destValue, dest_path)

        i = 0
        while i < len(start_path) and i < len(dest_path) and start_path[i] == dest_path[i]:
            i += 1

        up_moves = 'U' * (len(start_path) - i)

        remaining_moves = ''.join(dest_path[i:])
        
        return up_moves + remaining_moves
    

############################ Timewise best #########################################################
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        
        def find(node, val, path):
            if node.val == val:
                return True
            if node.left and find(node.left, val, path):
                path.append('L')
                return True
            if node.right and find(node.right, val, path):
                path.append('R')
                return True
            return False
        p1 = []
        p2 = []
        find(root, startValue, p1)
        find = find(root, destValue, p2)
        while p1 and p2 and p1[-1] == p2[-1]:
            p1.pop()
            p2.pop()
        return 'U' * len(p1) + ''.join(p2[::-1])
    
