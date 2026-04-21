# Last updated: 4/21/2026, 8:42:01 AM
class Solution:
    def reverseWords(self, s: str) -> str:
        l = [i for i in list(s.split(" ")) if i]
        l1 = l[::-1]
        s = " ".join(l1)
        return s
        