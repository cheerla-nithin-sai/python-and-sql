# Last updated: 4/20/2026, 1:26:28 PM
class Solution:
    def numTeams(self, r: List[int]) -> int:
        asc=0
        dec=0
        for i,ele in enumerate(r):
            low_left=high_left=low_right=high_right=0
            ## count no of elements less or high to left of picked ekement
            for k in r[:i]:
                if k<ele:
                    low_left+=1
                if k>ele:
                    high_left+=1
            
            for l in r[i+1:]:
                if l<ele:
                    low_right+=1
                if l>ele:
                    high_right+=1
            asc+=low_left*high_right
            dec+=high_left*low_right
        return asc+dec
                    
                