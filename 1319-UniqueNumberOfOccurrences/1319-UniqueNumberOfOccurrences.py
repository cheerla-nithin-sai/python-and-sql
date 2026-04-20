# Last updated: 4/20/2026, 1:27:17 PM
class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        d = Counter(arr)
        return len(set(arr))==len(set(d.values()))