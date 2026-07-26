# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        res = []
        q = deque([root])
        reverse = True

        while q:
            new_q = deque()
            level = []
            for node in q:
                level.append(node.val)
                if reverse:
                    if node.left:
                        new_q.appendleft(node.left)
                    if node.right:
                        new_q.appendleft(node.right)
                else:
                    if node.right:
                        new_q.appendleft(node.right)
                    if node.left:
                        new_q.appendleft(node.left)
            
            res.append(level)
            q = new_q
            reverse = not reverse
        
        return res