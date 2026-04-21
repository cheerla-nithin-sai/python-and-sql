# Last updated: 4/21/2026, 8:42:50 AM
class Solution:
    def isValid(self, s: str) -> bool:
        while "()" in s or "[]" in s or "{}" in s:
            s=s.replace("()","").replace("[]","").replace("{}","")
        return len(s)==0