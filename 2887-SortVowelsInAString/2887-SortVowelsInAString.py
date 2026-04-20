# Last updated: 4/20/2026, 1:24:52 PM
class Solution:
    def sortVowels(self, s: str) -> str:
        sl=list(s)
        vow=[]
        ind=[]
        c=["A","E","I","O","U","a","e","i","o","u"]
        for i in range(len(s)):
            if s[i] in c:
                vow.append(ord(s[i]))
                ind.append(i)
        vow.sort()

        for i in range(len(vow)):
            sl[ind[i]]=chr(vow[i])

        return "".join(sl)


        