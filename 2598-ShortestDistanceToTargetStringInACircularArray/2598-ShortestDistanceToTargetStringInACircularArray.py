# Last updated: 4/20/2026, 1:25:00 PM
class Solution:
    def closestTarget(self, words: List[str], target: str, startIndex: int) -> int:
        n=k=len(words)
        for i,j in enumerate(words):
            if j==target:
                k=min(k,abs(i-startIndex),n-abs(i-startIndex))
        return k if k<n else -1