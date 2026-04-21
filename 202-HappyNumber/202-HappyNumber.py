# Last updated: 4/21/2026, 8:41:34 AM
class Solution:
    def isHappy(self, n: int) -> bool:
        num = 0
        curr_num = n
        d ={}
        while True:
            for i in str(curr_num):
                num+=int(i)**2
            if num==1:
                return True
            if num in d:
                return False
            d[num]=0
            curr_num = num
            num =0
