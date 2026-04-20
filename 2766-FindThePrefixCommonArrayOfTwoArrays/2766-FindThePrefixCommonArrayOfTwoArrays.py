# Last updated: 4/20/2026, 1:24:53 PM
class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        l=[0]*len(A)
        for i in range(len(A)):
            c=0
            for j in range(i+1):
                for k in range(i+1):
                    if A[j]==B[k]:
                        c+=1
            l[i]=c
        return l
        