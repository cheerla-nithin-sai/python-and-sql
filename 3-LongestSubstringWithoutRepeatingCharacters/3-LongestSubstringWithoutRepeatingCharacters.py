# Last updated: 4/21/2026, 8:43:00 AM
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)==0:
            return 0
        n=len(s)
        max_len=float('-inf')
        l=0
        setx=set()
        for r in range(len(s)):
            if s[r] in setx:
                while l<r and s[r] in setx:
                    setx.remove(s[l])
                    l+=1
            setx.add(s[r])
            max_len=max(max_len,r-l+1)
        return max_len
