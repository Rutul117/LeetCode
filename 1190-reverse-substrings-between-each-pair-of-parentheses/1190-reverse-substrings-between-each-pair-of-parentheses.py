class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        ans = ""  

        for ch in s:
            if ch == '(':
                stack.append(ans)
                ans = ""
            elif ch == ')':
                ans = ans[::-1]
                ans = stack.pop() + ans
            else:
                ans += ch

        return ans 