# Last updated: 4/20/2026, 1:24:51 PM
class Solution:
    def checkStrings(self, s1: str, s2: str) -> bool:
        if len(s1)!=len(s2):
            return False
        s1_odd=[]
        s2_odd=[]
        s1_even=[]
        s2_even=[]
        for i in range(len(s1)):
            if i%2==0:
                s1_even.append(s1[i])
                s2_even.append(s2[i])
            else:
                s1_odd.append(s1[i])
                s2_odd.append(s2[i])
        print(s1_odd,s2_odd)
        return sorted(s1_odd)==sorted(s2_odd) and sorted(s1_even)==sorted(s2_even)