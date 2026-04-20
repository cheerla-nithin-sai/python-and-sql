# Last updated: 4/20/2026, 1:24:54 PM
class Solution:
    def minLength(self, s: str) -> int:
        while len(s)>0:
            if 'AB' in s:
                s = s.replace('AB',"")
            elif 'CD' in s:
                s = s.replace('CD',"")
            else:
                break
        return len(s)
        