class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left_pointer = 0
        right_pointer = n-1
        max_area = 0 

        while left_pointer < right_pointer:
            width = right_pointer - left_pointer
            h = min(height[left_pointer], height[right_pointer])
            area = width * h
            max_area = max(max_area, area)

            if height[left_pointer] < height[right_pointer]:
                left_pointer += 1
            else:
                right_pointer -= 1

        return max_area