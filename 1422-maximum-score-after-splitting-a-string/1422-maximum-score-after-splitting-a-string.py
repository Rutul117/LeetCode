class Solution:
    def maxScore(self, s: str) -> int:
        total_ones = s.count('1')
        max_score = 0
        left_zeros = 0 
        ones_seen = 0  
        
        for i in range(len(s) - 1):
            if s[i] == '0':
                left_zeros += 1
            else:
                ones_seen += 1
            
            right_ones = total_ones - ones_seen
            
            score = left_zeros + right_ones
            max_score = max(max_score, score)
        
        return max_score