# Last updated: 4/20/2026, 1:25:11 PM
class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        p=[]
        potions.sort()
        for i in spells:
            l = 0
            r = len(potions)-1
            total_nums = len(potions)

            while l<=r:
                m = l+(r-l)//2
                if i*potions[m]>=success:
                    total_nums=m
                    r=m-1
                else:
                    l=m+1
            p.append(len(potions)-total_nums)
        
        return p

        