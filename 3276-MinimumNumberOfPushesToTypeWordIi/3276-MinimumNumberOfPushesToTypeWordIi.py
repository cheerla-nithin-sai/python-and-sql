# Last updated: 4/20/2026, 1:24:39 PM
class Solution:
    def minimumPushes(self, word: str) -> int:
        c = sorted(Counter(word).values(),reverse=True)
        k = (  sum(c[  : 8]) + 2*sum(c[ 8:16]) + 3*sum(c[16:24]) + 4*sum(c[24: ]))
        return k