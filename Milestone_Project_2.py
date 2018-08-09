class Stack() :
	def __init__(self) :
		self.item = []
	def push(self, item) :
		self.item.append(item)
	def pop(self) :
		return self.item.pop()
	def peek(self):
		return self.item.peek()
if __name__ == "__main__":
    s1 = Stack()
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
print(s1.item)

