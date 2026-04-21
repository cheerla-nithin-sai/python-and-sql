# Last updated: 4/21/2026, 8:41:57 AM
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n=len(numbers)
        start=0
        end=n-1
        while start<end:
            s=numbers[start]+numbers[end]
            if s==target:
                return [start+1,end+1]
            elif s<target:
                start+=1
            else:
                end-=1
                
            
        