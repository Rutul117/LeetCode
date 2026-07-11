class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def helper(p, index):
            if index == len(nums):
                res.append(p)
                return
            
            ch = nums[index]
            for i in range(len(p)+1):
                helper(p[0:i] + [ch] + p[i:], index+1)
            
        helper([], 0)
        
        res = list(set(tuple(x) for x in res))
        res = [list(x) for x in res]
        return res