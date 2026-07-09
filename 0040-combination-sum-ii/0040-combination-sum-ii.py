class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort()
        result = []
        
        def backtrack(start, path, target):
            if target == 0:
                result.append(path)
                return
            if target < 0:
                return
            
            for i in range(start, len(candidates)):
                # Skip duplicates at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue
                
                # Include the current number and move forward
                backtrack(i + 1, path + [candidates[i]], target - candidates[i])
        
        backtrack(0, [], target)
        return result
