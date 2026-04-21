# Last updated: 4/21/2026, 8:42:44 AM
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        count = 0
        l = [-1]
        for i in range(len(s)):
            if s[i]=="(":
                l.append(i)
            else:
                l.pop()
                if not l:
                    l.append(i)
                else:
                    count=max(count,i-l[-1])
        return count

        