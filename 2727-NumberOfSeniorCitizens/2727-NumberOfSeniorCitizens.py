# Last updated: 4/20/2026, 1:24:56 PM
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        c=0
        for i in details:
            if int(i[11:13])>60:
                print(i)
                c+=1
        return c
        