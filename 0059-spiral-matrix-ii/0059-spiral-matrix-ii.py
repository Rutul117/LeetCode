class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:

        matrix = [[0 for _ in range(n)] for _ in range(n)]
        path = []
        visit = set()
        directions = [(0,1),(1,0),(0,-1),(-1,0)] 
        
        def spiral(row,col,d,num):
            
            matrix[row][col] = num
            visit.add((row,col))

            if num == n * n:
                return
            
            dr,dc = directions[d]
            nr,nc = row + dr,col + dc

            if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visit:
                spiral(nr,nc,d,num+1)
            else:
                d = (1 + d) % 4
                dr,dc = directions[d]
                spiral(row + dr,col + dc,d,num+1)

        spiral(0,0,0,1)

        return matrix
        