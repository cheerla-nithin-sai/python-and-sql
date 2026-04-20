# Last updated: 4/20/2026, 1:27:58 PM
class Solution:
    def lenLongestFibSubseq(self, arr: List[int]) -> int:
        s=set(arr)
        max_count=0
        n=len(arr)
        for first in range(n):
            for next in range(first+1,n):
                prev=arr[next]
                curr=arr[first]+arr[next]
                curr_len=2
                while curr in s:
                    prev,curr=curr,curr+prev
                    curr_len+=1
                    max_count=max(max_count,curr_len)
        return max_count


        