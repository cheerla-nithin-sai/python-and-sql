# Last updated: 4/20/2026, 1:25:03 PM
class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        if len(skill)==2:
            return skill[0]*skill[1]
        skill = sorted(skill)
        n =len(skill)
        total_sum = sum(skill)
        num = total_sum/(n/2)
        print(num)
        c=0
        l=0
        pro = 0
        r =len(skill)-1
        while l<=r:
            if skill[l]+skill[r]==num:
                c+=2
                pro = pro+(skill[l]*skill[r])
                print(skill[l],skill[r],pro)
            l+=1
            r-=1
        if pro==0 or c!=len(skill):
            return -1
        else:
            return pro
            


        