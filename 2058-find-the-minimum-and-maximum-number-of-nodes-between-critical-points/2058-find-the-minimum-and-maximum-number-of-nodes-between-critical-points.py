class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def nodesBetweenCriticalPoints(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: List[int]
        """
        if not head or not head.next or not head.next.next:
            return [-1, -1]
        
        critical_points = []
        index = 1
        prev = head
        curr = head.next
        next = curr.next
    
        while next:
            if (curr.val > prev.val and curr.val > next.val) or (curr.val < prev.val and curr.val < next.val):
                critical_points.append(index)
            
            prev = curr
            curr = next
            next = next.next
            index += 1
        
        if len(critical_points) < 2:
            return [-1, -1]
        
        max_distance = critical_points[-1] - critical_points[0]
        
        min_distance = float('inf')
        for i in range(1, len(critical_points)):
            min_distance = min(min_distance, critical_points[i] - critical_points[i - 1])
        
        return [min_distance, max_distance]
