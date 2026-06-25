class Solution:
    def maxArea(self, height: List[int]) -> int:
        length=len(height)
        left=0
        right=length-1
        area=(right-left)*min(height[left],height[right])
        maxheight=max(height)
        while left<right:
            if height[left]<height[right]:
                left+=1
            else:
                right-=1
            area=max((right-left)*min(height[left],height[right]),area)
            if area>=maxheight*(right-left):
                return area
        return area
        