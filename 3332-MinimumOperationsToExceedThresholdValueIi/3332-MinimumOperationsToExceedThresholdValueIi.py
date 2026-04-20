# Last updated: 4/20/2026, 1:24:37 PM
class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # i dont know heaps
        """count=0
        while min(nums)<k:
            nums.sort(reverse=True)
            a=nums.pop()
            b=nums.pop()
            c=min(a,b)*2+max(a,b)
            nums.append(c)
            count+=1
        return count"""
        heapq.heapify(nums)
        count=0
        while nums[0]<k:
            a=heapq.heappop(nums)
            b=heapq.heappop(nums)
            heapq.heappush(nums,min(a,b)*2+max(a,b))
            count+=1
        return count


