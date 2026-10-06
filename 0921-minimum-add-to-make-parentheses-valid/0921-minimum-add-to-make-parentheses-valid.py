class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        balance = 0
        additions = 0
        
        for char in s:
            if char == '(':
                balance += 1
            else:  # char == ')'
                balance -= 1
            
            if balance < 0:  # More closing brackets than opening
                additions += 1
                balance = 0  # Reset balance since we consider one addition
        
        # At the end, balance will tell how many opening brackets are unmatched
        return additions + balance