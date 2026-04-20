# Last updated: 4/20/2026, 1:24:21 PM
class Solution:
    def solveQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        # d={}
        # n=len(nums)
        # for i in range(n):
        #     if nums[i] not in d:
        #         d[nums[i]]=[i]
        #     else:
        #         d[nums[i]].append(i)
        # print(d)
        # l=[-1]*len(queries)
        # for j,i in enumerate(queries):
        #     if nums[i] in d.keys() and len(d[nums[i]])>1:
        #         first=(d[nums[i]][1]-d[nums[i]][0])
        #         sec=(d[nums[i]][-1]-d[nums[i]][0])
        #         third=n-(d[nums[i]][-1]-d[nums[i]][0])
        #         l[j]=min(first,sec,third)
        # return l
        n = len(nums)
        left = [0] * n
        right = [0] * n
        pos = {}

        for i in range(-n, n):
            if i >= 0:
                left[i] = pos.get(nums[i], -n)
            pos[nums[(i + n) % n]] = i

        pos.clear()
        for i in range(2 * n - 1, -1, -1):
            if i < n:
                right[i] = pos.get(nums[i], 2 * n)
            pos[nums[i % n]] = i

        for i in range(len(queries)):
            x = queries[i]
            if x - left[x] == n:
                queries[i] = -1
            else:
                queries[i] = min(x - left[x], right[x] - x)

        return queries