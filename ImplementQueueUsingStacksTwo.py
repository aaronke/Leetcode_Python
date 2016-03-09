class Queue:
	def _init_(self):
		self.inStack=[]
		self.outStack=[]

	def push(self,x):
		self.inStack.append(x)

	def pop(self):
		self.peek()
		self.outStack.pop()

	def peek(self):
		if not self.outStack:
			while self.inStack:
				self.outStack.append(self.inStack.pop())
		return self.outStack[-1]

	def empty(self):
		return len(self.inStack)+len(self.outStack())==0