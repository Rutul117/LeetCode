class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        
        # Helper function to perform backtracking
        def backtrack(current, open_count, close_count):
            # Base case: if the length of the current string is 2*n, add to result
            if len(current) == 2 * n:
                result.append(current)
                return
            
            # If we can add an open parenthesis, do so
            if open_count < n:
                backtrack(current + '(', open_count + 1, close_count)
            
            # If we can add a close parenthesis (only if it doesn't exceed open ones), do so
            if close_count < open_count:
                backtrack(current + ')', open_count, close_count + 1)
        
        # Start backtracking from an empty string with counts of open and close parentheses as 0
        backtrack('', 0, 0)
        
        return result