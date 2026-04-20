# Last updated: 4/20/2026, 1:24:31 PM
class Solution:
    def clearDigits(self, s: str) -> str:
        if s.isalpha():
            return s
        k=""
        for i in s:
            if i.isalpha():
                k+=i
            else:
                k=k[:-1]
        return k
        