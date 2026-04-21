# Last updated: 4/21/2026, 8:42:03 AM
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        l = ["+","*","-","/"]
        s=[]
        for i in tokens:
            if i not in l:
                s.append(int(i))
            else:
                num = s.pop()
                if i=="+":
                    s[-1]+=num
                elif i=="*":
                    s[-1]*=num
                elif i=="-":
                    s[-1]-=num
                else:
                    s[-1]=int(s[-1]/num)
        return s[0]
        
        