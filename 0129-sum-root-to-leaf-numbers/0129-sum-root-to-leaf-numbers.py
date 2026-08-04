# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(node, path_sum):
            if not node:
                return 0
            
            # Update the current path sum
            path_sum = path_sum * 10 + node.val
            
            # If it's a leaf node, return the path sum
            if not node.left and not node.right:
                return path_sum
            
            # Recursively calculate the sum for left and right subtrees
            left_sum = dfs(node.left, path_sum)
            right_sum = dfs(node.right, path_sum)
            
            # Return the sum of left and right subtrees
            return left_sum + right_sum
        
        # Start DFS from the root with an initial path sum of 0
        return dfs(root, 0)