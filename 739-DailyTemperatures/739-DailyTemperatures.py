# Last updated: 4/20/2026, 1:28:04 PM
class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        l = [0]*len(temp)
        stack = []
        for i in range(len(temp)):
            while stack and temp[stack[-1]]<temp[i]:
                index=stack.pop()
                l[index]=i-index
            stack.append(i)
        return l