# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        min_depth = 0
        if not root:
            return min_depth
        min_depth = 1
        q = deque([root])
        while q:
            n = len(q)
            for i in range(n):
                curr = q.popleft()
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if not curr.left and not curr.right:
                    return min_depth
            min_depth += 1
        return min_depth