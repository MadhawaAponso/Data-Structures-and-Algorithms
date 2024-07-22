# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return []

        averages = []
        queue = deque([root])

        while queue:
            level_sum = 0
            level_count = len(queue)

            for _ in range(level_count):
                node = queue.popleft()
                level_sum += node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            averages.append(level_sum / level_count)

        return averages
###################################################################################################################
class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        res = []
        level = [root]
        while level:
            nlevel = []
            avg = sum(n.val for n in level)/len(level)
            res.append(avg)
            for n in level:
                if n.left:
                    nlevel.append(n.left)
                if n.right:
                    nlevel.append(n.right)
            level = nlevel
        return res