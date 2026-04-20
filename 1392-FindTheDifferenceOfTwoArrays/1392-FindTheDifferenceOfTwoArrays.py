# Last updated: 4/20/2026, 1:27:13 PM
class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        s1 = set(nums1)
        s2= set(nums2)
        l = []
        l.append(list(s1-s2))
        l.append(list(s2-s1))
        return l