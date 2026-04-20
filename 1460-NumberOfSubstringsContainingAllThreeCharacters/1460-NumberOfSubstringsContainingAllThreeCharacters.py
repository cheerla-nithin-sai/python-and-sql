# Last updated: 4/20/2026, 1:26:37 PM
class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        a,b,c=-1,-1,-1
        count=0
        for i in range(len(s)):
            if s[i]=='a':
                a=i
            elif s[i]=='b':
                b=i
            else:
                c=i
            if a!=-1 and b!=-1 and c!=-1:
                count+=+min(a,b,c)+1
        return count
        