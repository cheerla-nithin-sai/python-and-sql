# Last updated: 4/21/2026, 8:40:56 AM
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_c,s1_len=Counter(s1),len(s1)
        for i in range(len(s2)-s1_len+1):
            s2_c=Counter(s2[i:i+s1_len])
            if s1_c==s2_c:
                return True
        return False

        