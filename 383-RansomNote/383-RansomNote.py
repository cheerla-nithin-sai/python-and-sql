# Last updated: 4/21/2026, 8:41:04 AM
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        l = list(ransomNote)
        for i in magazine:
            if i in l:
                l.remove(i)
        return len(l)==0
        