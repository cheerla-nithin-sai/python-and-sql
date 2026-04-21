# Last updated: 4/21/2026, 8:42:30 AM
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        n = 0
        for i in nums:
            if n<0:
                return False
            elif i>n:
                n=i
            n-=1
        return True
                
            
            
        