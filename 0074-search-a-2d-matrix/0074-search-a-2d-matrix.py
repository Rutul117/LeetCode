class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix or not matrix[0]:
            return False
        
        n = int(len(matrix[0]))

        for i in range(len(matrix)):
            if matrix[i][n-1] >= target:
                for j in range(n-1, -1, -1):
                    if matrix[i][j] == target:
                        return True

                break
        return False
                    