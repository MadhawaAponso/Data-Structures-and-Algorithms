# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def avg_(self,root):
        def traverse(root,values):
            if not root:
                return
            else:
                values.append(root.val)
                traverse(root.left,values)
                traverse(root.right,values)
        values = []
        traverse(root,values)
        if values:
            return sum(values) / len(values)
        else:
            return 0



    def averageOfSubtree(self, root: TreeNode) -> int:
        
        def traverse(root,count):
            if not root:
                return
            else:
                data = int(self.avg_(root))
                #print(count)
                if (data == root.val):
                    count.append(data)
                    #print(count)
                traverse(root.left,count)
                traverse(root.right,count)
            
        count = []
        traverse(root,count)
        print(count)
        return len(count)
        

######################TIME WISE most effective one#######################################
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        def traverse(root):
            if not root:
                return (0, 0, 0)  # (sum, count, matches)

            left_sum, left_count, left_matches = traverse(root.left)
            right_sum, right_count, right_matches = traverse(root.right)

            total_sum = left_sum + right_sum + root.val
            total_count = left_count + right_count + 1

            # Check if the current node's value equals the average of its subtree
            if total_sum // total_count == root.val:
                matches = 1
            else:
                matches = 0

            return (total_sum, total_count, left_matches + right_matches + matches)

        _, _, matches = traverse(root)
        return matches
    
##################################### SPacewise #####################################
class Solution:
    def averageOfSubtree(self, root: TreeNode) -> int:
        ans = [0]
        def dfs(node):
            if not node:
                return 0, 0 # (current sum, count)

            leftsum, leftcount = dfs(node.left)
            rightsum, rightcount = dfs(node.right)

            currsum = leftsum + rightsum + node.val
            currcount = leftcount + rightcount + 1

            if currsum//currcount == node.val:
                ans[0] = ans[0] + 1

            return currsum, currcount

        dfs(root)
        return ans[0]