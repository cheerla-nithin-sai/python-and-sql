# Last updated: 4/20/2026, 1:25:31 PM
class Solution:
    def smallestChair(self, times: List[List[int]], targetFriend: int) -> int:
        target = times[targetFriend]
        n =len(times)
        times.sort()
        chair_time = [0]*n
        for time in times:
            for i in range(n):
                if chair_time[i]<=time[0]:
                    chair_time[i]=time[1]
                    if time==target:
                        return i
                    break
        return 0
        