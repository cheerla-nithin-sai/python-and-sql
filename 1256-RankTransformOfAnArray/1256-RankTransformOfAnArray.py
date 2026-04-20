# Last updated: 4/20/2026, 1:27:28 PM
class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        r = {num:i+1 for i,num in enumerate(sorted(set(arr)))}
        return [r[num] for num in arr]


        