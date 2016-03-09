class ListNode(object):
	def _init_(self,x):
		self.val=x
		self.next=None

class Solution(object):
	def mergeTwoLists(self,l1,l2):
		dummy=ListNode(0)
		temp=dummy
		while l1 and l2:
			if l1.val<l2.val:
				temp.next=l1
				l1=l1.next
			else:
				temp.next=l2
				l2=l2.next
			temp=temp.next
		if l1:
			temp.next=l1
		if l2:
			temp.next=l2
		return dummy.next