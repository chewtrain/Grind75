class MyQueue:

    #if i put stuff here they will be class attributes which means all classes share the thing i put here

    def __init__(self):
        self.stack1=[]
        self.stack2=[]
        

    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        if not self.stack2:
            if not self.stack1:
                return None  
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()
        
        

    def peek(self) -> int:
        if not self.stack2:
            if not self.stack1:
                return None   
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2[-1]
        
        

    def empty(self) -> bool:
        return not (self.stack1 or self.stack2)


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()