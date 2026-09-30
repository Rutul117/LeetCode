class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        stack = []
        ans = []
        for i in range(len(seq)):
            if seq[i] == '(':
                ans.append(len(stack)%2)
                stack.append(len(stack))
            else:
                ans.append(stack.pop()%2)
        return ans