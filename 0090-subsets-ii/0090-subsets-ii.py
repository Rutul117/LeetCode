class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = [[]]
        
        for num in nums:
            new_subsets = []
            for subset in res:
                new_set = subset + [num]
                if new_set not in res:
                    new_subsets.append(new_set)
            res.extend(new_subsets)
        
        return res