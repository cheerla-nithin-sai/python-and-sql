# Last updated: 4/21/2026, 8:42:28 AM
class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = [str(i) for i in digits]
        num = "".join(s)
        num = str(int(num)+1)
        return [int(i) for i in num]   