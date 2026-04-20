# Last updated: 4/20/2026, 1:24:59 PM
class Solution:
    def maxKelements(self, nums: List[int], k: int) -> int:
        nums.sort()
        score=0
        while k>0:
            temp = nums.pop()
            score+=temp
            num = math.ceil(temp/3)
            nums.insert(bisect.bisect(nums,num),num)
            k-=1
        return score

        