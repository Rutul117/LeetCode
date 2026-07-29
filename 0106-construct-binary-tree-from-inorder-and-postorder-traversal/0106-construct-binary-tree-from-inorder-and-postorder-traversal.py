class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # Build a value → index map to avoid O(n) searches
        idx_map = {v: i for i, v in enumerate(inorder)}
        
        # Pointer to the last element in postorder (root)
        self.post_idx = len(postorder) - 1
        
        def build(l, r):
            # If no elements left in this inorder segment
            if l > r:
                return None
            
            # Root value from postorder
            root_val = postorder[self.post_idx]
            self.post_idx -= 1
            
            root = TreeNode(root_val)
            
            # Split inorder using index map
            mid = idx_map[root_val]
            
            # Critical: build right subtree first because postorder goes: left, right, root
            root.right = build(mid + 1, r)
            root.left = build(l, mid - 1)

            return root
        
        return build(0, len(inorder) - 1)
