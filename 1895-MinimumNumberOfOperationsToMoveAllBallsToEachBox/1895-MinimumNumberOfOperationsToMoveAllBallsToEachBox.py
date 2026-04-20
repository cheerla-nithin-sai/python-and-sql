# Last updated: 4/20/2026, 1:25:45 PM
class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        n=len(boxes)
        res=[0]*n
        val=0
        cnt=0
        for i in range(n):
            res[i]+=val
            if boxes[i]=='1':
                cnt+=1
            val+=cnt
        val=0
        cnt=0
        for i in range(n-1,-1,-1):
            res[i]+=val
            if boxes[i]=='1':
                cnt+=1
            val+=cnt
        return res