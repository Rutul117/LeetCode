class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        import math
        
        n = len(points)
        if n <= 2:
            return n
        
        best = 1
        
        for i in range(n):
            slopes = {}
            x1, y1 = points[i]
            
            for j in range(i + 1, n):
                x2, y2 = points[j]
                dy = y2 - y1
                dx = x2 - x1
                
                if dx == 0:
                    dy = 1
                elif dy == 0:
                    dx = 1
                else:
                    g = math.gcd(dy, dx)
                    dy //= g
                    dx //= g
                    # enforce consistent sign handling
                    if dx < 0:
                        dx = -dx
                        dy = -dy
                
                key = (dy, dx)
                slopes[key] = slopes.get(key, 1) + 1
                best = max(best, slopes[key])
        
        return best
