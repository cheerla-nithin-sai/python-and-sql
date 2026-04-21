# Last updated: 4/21/2026, 8:42:04 AM
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            if i not in d:
                d[i]=1
            else:
                d[i]+=1
        print(d)
        for i,j in d.items():
            if j==1:
                return i