# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        slow=head
        fast=head
        if head==None:
            return head
        while n>0:
            fast=fast.next
            n-=1
        if fast==None:
            head=head.next
            return head
        while fast.next:
            fast=fast.next
            slow=slow.next
        slow.next=slow.next.next
        return head
        