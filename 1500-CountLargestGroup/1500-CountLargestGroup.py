# Last updated: 4/20/2026, 1:26:29 PM
class Solution:
    def countLargestGroup(self, n: int) -> int:
        d={}
        for i in range(1,n+1):
            num=sum(int(i) for i in str(i))
            d[num]=d.get(num,0)+1
        return sum(1 for i in d.values() if i>=max(d.values()))

