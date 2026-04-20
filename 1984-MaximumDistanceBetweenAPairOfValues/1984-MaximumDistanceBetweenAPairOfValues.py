# Last updated: 4/20/2026, 1:25:39 PM
class Solution:
    def maxDistance(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        k=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]<=nums2[j]:
                k=max(j-i,k)
                j+=1
            else:
                i+=1 
                if i>j: j=i
        return k


