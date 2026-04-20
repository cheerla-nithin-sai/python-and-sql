# Last updated: 4/20/2026, 1:27:41 PM
class Solution:
    def removeDuplicates(self, s: str) -> str:
        l = []
        for i in s:
            if not l:
                l.append(i)
            elif l[-1]==i:
                l.pop()
            else:
                l.append(i)
        return "".join(l)
        