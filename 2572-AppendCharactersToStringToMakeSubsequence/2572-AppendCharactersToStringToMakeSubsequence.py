# Last updated: 4/20/2026, 1:25:04 PM
class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        i=0
        for char in s:
            if char==t[i]:
                i+=1
            if i==len(t):
                return 0
        return len(t)-i

        
        