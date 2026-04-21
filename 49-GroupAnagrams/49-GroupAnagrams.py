# Last updated: 4/21/2026, 8:42:37 AM
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d={}
        for i in range(len(strs)):
            s="".join(sorted(strs[i]))
            if s not in d.keys():
                d[s]=[strs[i]]
            else:
                d[s].append(strs[i])
        return list(d.values())

        