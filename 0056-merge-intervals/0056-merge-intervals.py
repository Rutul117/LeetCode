class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()  # sort by start
        
        merged = []
        
        for start, end in intervals:
            # If merged list is empty OR non-overlapping interval
            if not merged or merged[-1][1] < start:
                merged.append([start, end])
            else:
                # Overlap → merge by extending the end
                merged[-1][1] = max(merged[-1][1], end)
        
        return merged