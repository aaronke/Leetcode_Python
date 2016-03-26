# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        dummy=ListNode(0)
        dummy.next=head
        p=dummy
        i=1
        while i<m:
            p=p.next
            i+=1
        i=0
        pre=p.next
        cur=pre.next
        while i<n-m:
            temp=cur.next
            cur.next=pre
            pre=cur
            cur=temp
            i+=1
        p.next.next=cur
        p.next=pre
        return dummy.next
            
            
            
        