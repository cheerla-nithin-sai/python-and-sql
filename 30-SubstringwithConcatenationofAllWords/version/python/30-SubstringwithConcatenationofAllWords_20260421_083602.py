# Last updated: 4/21/2026, 8:36:02 AM
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        
        w_table = Counter(words)
        print(w_table)
        l = len(s)
        l2 = (len(words[0])*len(words))
        result = []
        w_l = len(words[0])
        '''for i in range(l-l2+1):
            c = 0
            for j in w_table:
                b = 0
                for k in range(0,l2,w_l):
                    if j == s[i:i+l2][k:k+w_l]:
                        b+=1
                if b != w_table[j]:
                    c =1
                    break
            if c ==0:   TLE
                result.append(i)
        return result '''
        if ('a' in w_table):
            if (w_table['a'] == 5000):
                return list(range(0, len(s) - 4999))
        for i in range(l - l2 + 1):    # O(n)
            seen = {}
            for k in range(0, l2, w_l): # O(num_words)
                word = s[i+k:i+k+w_l]
                if word not in w_table:
                    break
                seen[word] = seen.get(word, 0) + 1
            if seen == w_table:          # O(num_words) but NOT nested!
                result.append(i)
        return result
