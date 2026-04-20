# Last updated: 4/20/2026, 1:26:21 PM
class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        target.sort()
        arr.sort()
        for i in range(len(arr)):
            if arr[i]!=target[i]:
                return False
        return True
        