# Last updated: 4/21/2026, 8:41:05 AM
# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        low,upper = 0,n
        while low<=upper:
            mid = (low+upper)//2
            num = guess(mid)
            if num<0:
                upper = mid-1
                
            elif num>0:
                low = mid+1
            else:
                return mid
        