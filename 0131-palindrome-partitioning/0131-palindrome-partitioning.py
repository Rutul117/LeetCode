class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def is_palindrome(sub):
            return sub == sub[::-1]

        def backtrack(start, path):
            if start == len(s):
                result.append(path[:])
                return
            for end in range(start + 1, len(s) + 1):
                if is_palindrome(s[start:end]):
                    path.append(s[start:end])
                    backtrack(end, path)
                    path.pop()
        
        result = []
        backtrack(0, [])
        return result

# Example usage:
sol = Solution()
print(sol.partition("aab"))  # Output: [["a","a","b"],["aa","b"]]
print(sol.partition("a"))    # Output: [["a"]]
