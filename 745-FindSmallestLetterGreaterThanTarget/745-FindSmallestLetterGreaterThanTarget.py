# Last updated: 4/20/2026, 1:28:03 PM
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        for i in letters:
            if i>target:
                return i
        return letters[0]
        