# Last updated: 4/21/2026, 8:42:06 AM
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas)-sum(cost)<0:
            return -1
        start=0
        gas_req=0
        for i in range(len(gas)):
            gas_req+=gas[i]-cost[i]

            if gas_req<0:
                start=i+1
                gas_req=0
        return start
        