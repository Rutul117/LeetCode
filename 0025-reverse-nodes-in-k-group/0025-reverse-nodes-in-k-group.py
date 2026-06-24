# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverseLinkedList(start, end):
            prev = None
            current = start
            while current != end:
                temp = current.next
                current.next = prev
                prev = current
                current = temp
            return prev

        def getLength(node):
            length = 0
            while node:
                length += 1
                node = node.next
            return length

        length = getLength(head)
        dummy = ListNode(0)
        dummy.next = head
        current = dummy

        while length >= k:
            start = current.next
            end = current.next
            for _ in range(k):
                end = end.next

            current.next = reverseLinkedList(start, end)
            start.next = end
            current = start
            length -= k

        return dummy.next