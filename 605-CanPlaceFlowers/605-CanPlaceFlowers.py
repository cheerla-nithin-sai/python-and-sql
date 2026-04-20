# Last updated: 4/20/2026, 1:28:29 PM
class Solution:
    def canPlaceFlowers(self, arr: List[int], n: int) -> bool:
        c=0
        for i in range(len(arr)):
            if arr[i]==0:
                l = (i==0) or (arr[i-1]==0)
                r = (i==len(arr)-1) or (arr[i+1]==0)
                if l and r:
                    arr[i]=1
                    c+=1
                    if c>=n:
                        return True
        return c>=n
                
            
        