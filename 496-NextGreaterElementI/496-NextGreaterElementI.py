# Last updated: 4/21/2026, 8:40:57 AM
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        l = [-1]*len(nums1)
        for i in range(len(nums1)):
            k = nums2.index(nums1[i])
            while k<len(nums2):
                if nums2[k]>nums1[i]:
                    l[i]=nums2[k]
                    break
                k+=1
        return l
            