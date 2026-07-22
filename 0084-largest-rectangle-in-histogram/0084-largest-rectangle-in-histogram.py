class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)   # sentinel to flush the stack
        stack = []          # will store indices
        max_area = 0

        for i, h in enumerate(heights):
            # maintain increasing stack
            while stack and heights[stack[-1]] > h:
                height = heights[stack.pop()]
                # width = current index i minus the index after the previous bar
                width = i if not stack else i - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(i)

        return max_area
