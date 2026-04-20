# Last updated: 4/20/2026, 1:25:16 PM
class Solution:
    def checkString(self, s: str) -> bool:
        l=[]
        for i in s:
            if i=="b":
                l.append(i)
            elif l and i=="a":
                return False
        return True
            