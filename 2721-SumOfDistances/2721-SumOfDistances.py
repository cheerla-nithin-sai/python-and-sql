# Last updated: 4/23/2026, 7:56:51 AM
class Solution:
    def distance(self, nums: List[int]) -> List[int]:
        d={}
        n=len(nums)
        for i in range(n):
            if nums[i] not in d:
                d[nums[i]]=[i]
            else:
                d[nums[i]].append(i)
        l=[0]*n
        for key,indexes in d.items():
            pre,p=0,0
            suf=sum(indexes)
            s=len(indexes)
            for idx in indexes:
                p+=1
                pre+=idx
                suf-=idx
                s-=1
                l[idx]=(-pre+p*idx-s*idx+suf)
        return l
