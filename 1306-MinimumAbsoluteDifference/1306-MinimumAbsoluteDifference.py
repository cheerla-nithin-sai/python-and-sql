# Last updated: 4/20/2026, 1:27:20 PM
class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        m=float('inf')
        arr.sort()
        for i in range(len(arr)-1):
            m=min(m,arr[i+1]-arr[i])
        return [[arr[i],arr[i+1]] for i in range(len(arr)-1) if arr[i+1]-arr[i]==m]
        