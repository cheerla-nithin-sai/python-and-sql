# Last updated: 4/21/2026, 8:42:58 AM
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows==1:
            return s

        r=[""]*numRows
        a=0
        b=1
        for i in s:
            r[a]+=i
            if a==0:
                b=1
            elif a==numRows-1:
                b=-1
            a+=b
        return "".join(r)
        