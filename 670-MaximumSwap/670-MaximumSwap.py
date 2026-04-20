# Last updated: 4/20/2026, 1:28:13 PM
class Solution:
    def maximumSwap(self, num: int) -> int:
        k = list(str(num))
        for i in range(len(k)-1):
            if k[i]<max(k[i+1:]):
                b = len(k)-1-k[::-1].index(max(k[i+1:]))
                k[i],k[b]=k[b],k[i]
                print(k)
                break
        a = "".join(k)
        return int(a)
        