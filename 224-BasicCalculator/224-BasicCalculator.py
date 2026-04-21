# Last updated: 4/21/2026, 8:41:27 AM
class Solution:
    def calculate(self, s: str) -> int:
        num =0
        sign =1
        res =0
        nums = []
        for i in s:
            if i.isdigit():
                num=num*10+int(i)
            elif i in ["-","+"]:
                res = res+num*sign
                num=0
                if i=="-":
                    sign = -1
                else:
                    sign =1
            elif i =="(":
                nums.append(res)
                nums.append(sign)
                sign = 1
                res=0
            elif i==")":
                res+=sign*num
                res*=nums.pop()
                res+=nums.pop()
                num =0
        return res+num*sign
        