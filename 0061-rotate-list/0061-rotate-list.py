class Solution:
    def rotateRight(self, head, k):
        if not head or not head.next:
            return head

        # length
        c = 1
        temp = head
        while temp.next!=None:
            c += 1
            temp = temp.next

        k = k % c
        if k == 0:
            return head

        
        temp.next=head

        new_tail=head
        steps=c-k
        for i in range(steps-1):
            new_tail=new_tail.next
        new_head=new_tail.next
        new_tail.next=None
        return new_head