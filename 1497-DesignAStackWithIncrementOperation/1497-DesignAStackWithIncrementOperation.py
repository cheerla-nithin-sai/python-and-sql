# Last updated: 4/20/2026, 1:26:31 PM
class CustomStack:

    def __init__(self, maxSize: int):
        self.stack = []
        self.m = maxSize

    def push(self, x: int) -> None:
        if len(self.stack)<self.m:
            self.stack.append(x)
        

    def pop(self) -> int:
        if self.stack:
            return self.stack.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        n = min(len(self.stack),k)
        for i in range(n):
            self.stack[i]+=val

        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)