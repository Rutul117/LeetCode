class Solution:
    def checkOverlap(self, radius: int, xCenter: int, yCenter: int,
                     x1: int, y1: int, x2: int, y2: int) -> bool:
        
        # Clamp circle center to rectangle boundaries
        closestX = min(max(xCenter, x1), x2)
        closestY = min(max(yCenter, y1), y2)

        # Compute squared distance (cheaper than sqrt)
        dist_sq = (closestX - xCenter) ** 2 + (closestY - yCenter) ** 2

        return dist_sq <= radius ** 2