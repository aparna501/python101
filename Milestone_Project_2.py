#Milestone_Project_2
class StackEmptyExcept() :
	def __init__(self) :
		self.item = []
	def push(self, item) :
		self.item.append(item)
	def pop(self) :
		try:
			return self.item.pop()
		except IndexError:
			print("sorry,there is an error")
	def peek(self):
		n=len(self.item)
		return self.item[n-1]


s1= StackEmptyExcept()
s1.push(1)
print(s1.peek())
s1.push(2)
print(s1.peek())
s1.push(3)
print(s1.peek())
s1.push(4)
print(s1.peek())
s1.push(5)
print(s1.peek())
s1.push(6)
print(s1.peek())
s1.push(7)
print(s1.peek())
s1.pop()
s1.push(8)
s1.pop()
s1.peek()

'''output:
1
2
3
4
5
6
'''

#Queue Implementation

class Queue:
	def __init__(self):
		self.items = []

	def isEmpty(self):
		return self.items == []

	def enqueue(self, item):
		self.items.insert(0,item)

	def dequeue(self):
		return self.items.pop()
	
	def size(self):
		return len(self.items)

	def isEmpty(self):
		return self.items == []

	def printqueue(self):
		for items in self.items:
			print(items)

q1 = Queue()
print(q1.isEmpty())
q1.enqueue('Apple')
q1.enqueue(7)
q1.enqueue('Python')
q1.enqueue('World')
q1.printqueue()
q1.dequeue()
q1.printqueue()
print(q1.size())

'''
output:True
       Python
       7
       Apple
       
       2'''