# Last updated: 4/20/2026, 1:27:08 PM
class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        d=defaultdict(list)
        for i in arr:
            k=0
            d[sum([k+1 for j in format(i,'b') if j=='1'])].append(i)
        return [i for k in sorted(d.keys()) for i in sorted(d[k])]
        