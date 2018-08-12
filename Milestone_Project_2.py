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
s1.pop()

'''output:
1
2
3
4
5
6
'''

