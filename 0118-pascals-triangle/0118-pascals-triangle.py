class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        
        for _ in range(1, numRows):
            prev = res[-1]
            row = [1]
            
            for j in range(1, len(prev)):
                row.append(prev[j - 1] + prev[j])
            
            row.append(1)
            res.append(row)
        
        return res
