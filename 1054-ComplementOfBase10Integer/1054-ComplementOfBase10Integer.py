# Last updated: 4/20/2026, 1:27:45 PM
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        k=[]
        for i in list(format(n,'b')):
            if i=='1':
                k.append('0')
            else:
                k.append('1')
        return int("".join(k),2)
        