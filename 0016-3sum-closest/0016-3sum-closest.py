class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        best = float('inf')

        for i in range(len(nums) - 2):
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = nums[i] + nums[l] + nums[r]
                
                # Update best if this sum is closer
                if abs(s - target) < abs(best - target):
                    best = s

                # Move pointers strategically
                if s < target:
                    l += 1
                elif s > target:
                    r -= 1
                else:
                    # Perfect hit — immediate return
                    return s
        
        return best
