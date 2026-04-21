# Last updated: 4/21/2026, 8:41:09 AM
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        n=len(s)
        for i in range(n//2):
            print(s[i])
            print(s[n-i-1])
            s[i],s[n-i-1]=s[n-i-1],s[i]

        