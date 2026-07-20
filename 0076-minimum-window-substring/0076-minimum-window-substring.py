from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        # Step 1: Create a counter for the characters in t
        t_count = Counter(t)
        required_chars = len(t_count)
        
        # Step 2: Initialize left and right pointers, and other variables
        left = right = 0
        formed = 0
        window_counts = {}
        ans = float('inf'), None, None
        
        # Step 3: Move the right pointer to form a window
        while right < len(s):
            char = s[right]
            window_counts[char] = window_counts.get(char, 0) + 1
            if char in t_count and window_counts[char] == t_count[char]:
                formed += 1
            
            # Step 4: Move the left pointer to minimize the window size
            while left <= right and formed == required_chars:
                char = s[left]
                if right - left + 1 < ans[0]:
                    ans = (right - left + 1, left, right)
                window_counts[char] -= 1
                if char in t_count and window_counts[char] < t_count[char]:
                    formed -= 1
                left += 1
            
            right += 1
        
        return "" if ans[0] == float('inf') else s[ans[1]: ans[2] + 1]

# Test cases
solution = Solution()
print(solution.minWindow("ADOBECODEBANC", "ABC"))  # Output: "BANC"
print(solution.minWindow("a", "a"))               # Output: "a"
print(solution.minWindow("a", "aa"))              # Output: ""
