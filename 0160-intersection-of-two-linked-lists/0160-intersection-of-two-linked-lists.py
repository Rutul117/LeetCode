class Solution(object):
    def getIntersectionNode(self, headA, headB):
        n = 0
        pA = headA
        while pA:
            n += 1
            pA = pA.next
        
        m = 0
        pB = headB
        while pB:
            m += 1
            pB = pB.next

        diff = abs(n - m)

        if n > m:
            headA, headB = headB, headA

        for i in range(diff):
            headB = headB.next

        pA = headA
        pB = headB

        while pA != pB:
            pA = pA.next
            pB = pB.next
        return pA

