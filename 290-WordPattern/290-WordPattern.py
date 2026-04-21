# Last updated: 4/21/2026, 8:41:11 AM
class Solution:
    def wordPattern(self, pattern: str, k: str) -> bool:
        if len(k.split())!=len(pattern) or len(set(k.split())) != len(set(pattern)):
            return False
        s = list(k.split())
        d = {}
        for i in range(len(pattern)):
            if s[i] not in d:
                d[s[i]]=pattern[i]
            else:
                if d[s[i]]!=pattern[i]:
                    return False
        return True
                
        