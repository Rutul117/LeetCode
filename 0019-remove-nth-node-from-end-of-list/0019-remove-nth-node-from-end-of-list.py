class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy

        # Move the first pointer ahead by n+1 steps
        for _ in range(n + 1):
            first = first.next

        # Move first to the end, maintaining the gap
        while first is not None:
            first = first.next
            second = second.next

        # Remove the nth node from the end
        second.next = second.next.next

        return dummy.next

# Example usage:
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

solution = Solution()
result = solution.removeNthFromEnd(head, 2)

# Print the resulting linked list
while result:
    print(result.val)
    result = result.next