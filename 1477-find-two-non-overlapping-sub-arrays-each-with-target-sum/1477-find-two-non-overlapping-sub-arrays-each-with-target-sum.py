class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        
		
		
        
        def get_sub_arrays( arr ):
            lookup = collections.defaultdict(int)
            running_sum = 0
            dp = [float('inf')] * len(arr)
            
            for i, num in enumerate(arr):
                running_sum += num
                if running_sum == target:
                    dp[i] = i - 0 + 1
                elif running_sum - target in lookup:
                    dp[i] = i - lookup[running_sum - target] + 1
                lookup[running_sum] = i+1
                dp[i] = min( dp[i-1], dp[i] )
            return dp
        
        dp_left = get_sub_arrays( arr )                     # from front
        dp_right = get_sub_arrays( arr[::-1] )[::-1]        # from backwards
        
        ans = float('inf')
        for i in range( 1, len(arr) ):
            ans = min( ans, dp_left[i-1] + dp_right[i] )
        return ans if( ans != float('inf') ) else -1