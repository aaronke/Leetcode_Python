def reverseList(self,head):
	dummy=ListNode(0)
	while head:
		next=head.next
		head.next=null
		dummy.next=head
		head=next
	return dummy.next