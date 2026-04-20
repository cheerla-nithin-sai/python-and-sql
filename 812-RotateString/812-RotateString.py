# Last updated: 4/20/2026, 1:27:59 PM
class Solution:
    def rotateString(self, s: str, goal: str) -> bool:
        for i in range(len(goal)):
            k=s[i:]+s[:i]
            if k==goal:
                return True
        return False
        