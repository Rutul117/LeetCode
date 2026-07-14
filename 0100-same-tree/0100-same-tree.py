# class Solution(object):
#     def isSameTree(self, p, q):
#         """
#         :type p: TreeNode
#         :type q: TreeNode
#         :rtype: bool
#         """
#         # If both nodes are None, they are considered the same
#         if not p and not q:
#             return True
#         # If one of the nodes is None or the values are different, they are not the same
#         if not p or not q or p.val != q.val:
#             return False
#         # Recursively check left and right subtrees
#         return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        stack = [(p, q)]
        while stack:
            node1, node2 = stack.pop()
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))
        return True