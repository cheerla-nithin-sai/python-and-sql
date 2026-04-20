# Last updated: 4/20/2026, 1:28:12 PM
class Solution:
    def validPalindrome(self, s: str) -> bool:
        l=0
        r=len(s)-1
        while l<r:
            if s[l]!=s[r]:
                k=s[l+1:r+1]
                x=s[l:r]
                return k==k[::-1] or x==x[::-1]
            l+=1
            r-=1
        return True        