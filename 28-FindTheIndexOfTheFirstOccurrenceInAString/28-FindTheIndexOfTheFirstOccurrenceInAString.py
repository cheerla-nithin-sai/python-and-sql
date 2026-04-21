# Last updated: 4/21/2026, 8:42:46 AM
class Solution:
    def strStr(self, S1: str, S2: str) -> int:
        for i in range(len(S1)):
            for j in range(i,len(S1)):
                if S1[i:j+1]==S2:
                    return i
        return -1