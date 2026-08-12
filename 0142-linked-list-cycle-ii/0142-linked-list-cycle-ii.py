class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        start=head
        lookup=set()
        while start:
            if start in lookup:
                return start
            else:
                lookup.add(start)
                start=start.next
        return None