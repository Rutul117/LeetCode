# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        gods_amazing = []
        curr = head

        # adding node values to the array
        while curr:
            gods_amazing.append(curr.val)
            curr = curr.next

        # sorting the values
        gods_amazing.sort()

        # replacing the values with the sorted ones
        curr = head
        for i in range(len(gods_amazing)):
            curr.val = gods_amazing[i]
            curr = curr.next

        return head