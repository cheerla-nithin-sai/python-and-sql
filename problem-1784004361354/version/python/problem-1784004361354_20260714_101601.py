# Last updated: 7/14/2026, 10:16:01 AM
1class Solution:
2    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
3        from datetime import datetime
4        DT=datetime.strptime(endTime, "%H:%M:%S") - datetime.strptime(startTime, "%H:%M:%S")
5        return int(DT.total_seconds())
6        