# Last updated: 4/20/2026, 1:26:08 PM
class Solution:
    def minimumDeletions(self, s: str) -> int:
        count =0
        l = []
        for i in s:
            if i=="b":
                l.append(i)
            elif l:
                l.pop()
                count+=1
        return count