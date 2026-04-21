# Last updated: 4/21/2026, 8:42:59 AM
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l=sorted(nums1+nums2)
        mid=len(l)//2
        if len(l)%2==0:
            return (l[mid]+l[mid-1])/2.0
        else:
            return float(l[mid])
        