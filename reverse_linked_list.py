def reverseList(self,head):
	dummy=ListNode(0)
	while head:
		next=head.next
		head.next=dummy.next
		dummy.next=head
		head=next
	return dummy.next