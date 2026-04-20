# Last updated: 4/20/2026, 1:25:18 PM
class Solution:
    def countMaxOrSubsets(self, nums: List[int]) -> int:
        max_or = 0
        prev = Counter()
        prev[0] = 1
        
        for elem in nums:
            max_or |= elem

            current = Counter()
            for prev_or, cnt in prev.items():
                current[prev_or | elem] += cnt
            prev.update(current)
        
        return prev[max_or]
    