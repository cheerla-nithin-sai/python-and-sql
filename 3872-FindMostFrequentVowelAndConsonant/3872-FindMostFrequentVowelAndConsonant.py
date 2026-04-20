# Last updated: 4/20/2026, 1:24:14 PM
class Solution:
    def maxFreqSum(self, s: str) -> int:
        d=Counter(s)
        vow=["a","e","i","o","u"]
        max_vow=0
        max_con=0
        for i in d.keys():
            if i in vow:
                max_vow=max(max_vow,d[i])
            else:
                max_con=max(max_con,d[i])
        return max_vow+max_con
        