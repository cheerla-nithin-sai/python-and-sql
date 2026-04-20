# Last updated: 4/20/2026, 1:26:10 PM
class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        l = [0]*len(code)
        if k==0:
            return l
        for i in range(len(code)):
            if k>0:
                for j in range(i+1,i+k+1):
                    l[i]+=code[j%len(code)]
            else:
                for j in range(i-abs(k),i):
                    l[i]+=code[(j+len(code))%len(code)]        
        return l