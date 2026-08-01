class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next

class Solution:
    def connect(self, root: 'Node') -> 'Node':
        if not root:
            return None
        
        # Start with the root node
        current = root
        
        while current:
            dummy = Node(0)  # Dummy node for the next level
            tail = dummy  # Tail pointer to build the next level's linked list
            
            while current:
                if current.left:
                    tail.next = current.left
                    tail = tail.next
                if current.right:
                    tail.next = current.right
                    tail = tail.next
                current = current.next  # Move to the next node at the current level
            
            current = dummy.next  # Move to the next level
        
        return root
