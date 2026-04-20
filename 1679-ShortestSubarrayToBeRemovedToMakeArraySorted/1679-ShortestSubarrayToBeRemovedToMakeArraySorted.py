# Last updated: 4/20/2026, 1:26:12 PM
class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        l=0
        r=len(arr)-1
        n=len(arr)
        while l<n-1 and arr[l]<=arr[l+1]:
            l+=1
        while r>0 and arr[r-1]<=arr[r]:
            r-=1
        if r<=l:
            return 0
        ans=min(n-l-1,r)
        i,j=0,r
        while i<=l and j<n:
            if arr[i]<=arr[j]:
                ans=min(ans,j-i-1)
                i+=1
            else:
                j+=1
        return ans

        