class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        
        stack, output = [], []
        last_visited = None
        current = root
        
        while stack or current:
            if current:
                stack.append(current)
                current = current.left
            else:
                peek_node = stack[-1]
                if peek_node.right and last_visited != peek_node.right:
                    current = peek_node.right
                else:
                    output.append(peek_node.val)
                    last_visited = stack.pop()
        
        return output
