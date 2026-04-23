# Last updated: 4/23/2026, 7:55:02 AM
1class Solution:
2    def distance(self, nums: List[int]) -> List[int]:
3        d={}
4        n=len(nums)
5        for i in range(n):
6            if nums[i] not in d:
7                d[nums[i]]=[i]
8            else:
9                d[nums[i]].append(i)
10        l=[0]*n
11        for key,indexes in d.items():
12            pre,p=0,0
13            suf=sum(indexes)
14            s=len(indexes)
15            for idx in indexes:
16                p+=1
17                pre+=idx
18                suf-=idx
19                s-=1
20                l[idx]=(-pre+p*idx-s*idx+suf)
21        return l
22