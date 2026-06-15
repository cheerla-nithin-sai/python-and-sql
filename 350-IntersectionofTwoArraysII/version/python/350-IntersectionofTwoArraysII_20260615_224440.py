# Last updated: 6/15/2026, 10:44:40 PM
1class Solution:
2    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
3        nums1.sort()
4        nums2.sort()
5        i,j=0,0
6        res=[]
7        while i<len(nums1) and j<len(nums2):
8            if nums1[i]==nums2[j]:
9                res.append(nums1[i])
10                i+=1
11                j+=1
12            elif nums1[i]<nums2[j]:
13                i+=1
14            else:
15                j+=1
16        return res
17