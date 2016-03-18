# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head==None:
            return head
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        while p.next!=None and p.next.next!=None:
            t1=p
            p=p.next
            t1.next=p.next
            
            t2=p.next.next
            p.next.next=p
            p.next=t2
        return dummy.next
        