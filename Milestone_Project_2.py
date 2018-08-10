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


    s1 = StackEmptyExcept()
    s1.push(1)
    s1.push(2)
    s1.push(3)
    s1.push(4)
    s1.push(5)
    s1.push(6)
    s1.push(7)
    s1.push(8)
    s1.push(8)
    s1.pop()


'''output:
[1,2,3,4,5,6,7,8]'''

