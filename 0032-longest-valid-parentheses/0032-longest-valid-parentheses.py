class Solution(object):
    def longestValidParentheses(self, s: str) -> int:
        """
        :type s: str
        :rtype: int
        """
        stack = [-1]  # Initialize stack with -1 to handle edge case of starting with ')'
        max_length = 0

        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                # Pop the last opening parenthesis
                stack.pop()

                if not stack:
                    # If the stack is empty, push the current index
                    stack.append(i)
                else:
                    # Update the maximum length
                    max_length = max(max_length, i - stack[-1])

        return max_length