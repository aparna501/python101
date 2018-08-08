class Stack() :

   def __init__(self) :
    self.items = [1,2,3,4,5,6,7]
   def push(self, item) :
    self.items.append(item)

   def pop(self) :
    return self.items.pop()


if __name__ == "__main__":
    demoStack = Stack()
    demoStack.push(8)
    demoStack.push(9)
    demoStack.push(9)
    demoStack.pop()
    print(demoStack.items)