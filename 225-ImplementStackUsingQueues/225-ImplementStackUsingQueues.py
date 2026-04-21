# Last updated: 4/21/2026, 8:41:26 AM
class MyStack:

    def __init__(self):
        self.stack1=[]
        self.queue2=[]
        
    def push(self, x: int) -> None:
        self.stack1.append(x)
        
    def pop(self) -> int:
        if len(self.stack1)>0:
            return self.stack1.pop()
        else:
            return -1

    def top(self) -> int:
        if len(self.stack1)>0:
            return self.stack1[-1]
        else:
            return -1

    def empty(self) -> bool:
        return len(self.stack1)==0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()