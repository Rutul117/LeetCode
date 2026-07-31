class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: 'TreeNode') -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root:
            return
        
        stack = [root]
        prev = None
        
        while stack:
            node = stack.pop()
            
            if prev:
                prev.right = node
                prev.left = None
            
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)
            
            prev = node