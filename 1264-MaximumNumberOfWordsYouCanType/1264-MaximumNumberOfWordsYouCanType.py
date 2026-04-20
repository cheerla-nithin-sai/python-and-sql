# Last updated: 4/20/2026, 1:27:27 PM
class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        c=0
        check=set(list(brokenLetters))
        for word in text.split():
            for j in check:
                if j in word:
                    c+=1
                    break
        return len(text.split())-c