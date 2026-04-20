# Last updated: 4/20/2026, 1:27:31 PM
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        l=[]
        nl=[]
        for i in arr2:
            for j in arr1:
                if j==i:
                    l.append(i)
        for i in arr1:
            if i not in l:
                nl.append(i)
        nl.sort()
        return l+nl
        