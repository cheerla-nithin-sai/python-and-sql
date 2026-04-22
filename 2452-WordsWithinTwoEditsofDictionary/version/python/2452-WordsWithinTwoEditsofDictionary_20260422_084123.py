# Last updated: 4/22/2026, 8:41:23 AM
1class Solution:
2    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
3        l=[]
4        for word in queries:
5            for match in dictionary:
6                d=0
7                for j in range(len(word)):
8                    if word[j]!=match[j]:d+=1
9                if d<=2:
10                    l.append(word)
11                    break
12        return l
13
14
15