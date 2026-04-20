# Last updated: 4/20/2026, 1:25:12 PM
class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        c=0
        for i in words:
            if len(i)>=len(pref) and pref==i[:len(pref)]:
                c+=1
        return c