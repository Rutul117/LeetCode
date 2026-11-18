class Solution:
    def minChanges(self, s: str) -> int:
        # The length of the string is guaranteed to be even.
        n = len(s)
        changes = 0
        
        # We will iterate through the string in pairs
        for i in range(0, n, 2):
            # Check the current pair of characters
            if s[i] != s[i + 1]:
                changes += 1  # We need to change one of them to make them equal
        
        return changes
