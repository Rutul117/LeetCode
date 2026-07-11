from heapq import heappush, heappop

class Solution:
    def scheduleCourse(self, courses: List[List[int]]) -> int:
        courses.sort(key=lambda x: x[1])

        heap = []
        time = 0

        for duration, lastDay in courses:
            time += duration
            heappush(heap, -duration)

            if time > lastDay:
                time += heappop(heap)

        return len(heap)