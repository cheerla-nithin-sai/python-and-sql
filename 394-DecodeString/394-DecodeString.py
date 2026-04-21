# Last updated: 4/21/2026, 8:41:01 AM
class Solution:
    def decodeString(self, s: str) -> str:
        l=[]
        for i in s:
            if i!="]":
                l.append(i)
            else:
                st=""
                while l[-1]!="[":
                    st=l.pop()+st
                l.pop()
                num=""
                while l and l[-1].isdigit():
                    num=l.pop()+num
                st=int(num)*st
                l.append(st)
        return "".join(l)
