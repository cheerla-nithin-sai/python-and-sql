# Last updated: 4/20/2026, 1:28:08 PM
class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        d = {}
        for index,value in enumerate(nums):
            if value in d:
                d[value].append(index)
            else:
                d[value]=[index]
        max_degree = max([len(i) for i in d.values()])
        len_short_subarray = min([i[-1]-i[0] for i in d.values() if len(i)==max_degree])
        return len_short_subarray+1
        