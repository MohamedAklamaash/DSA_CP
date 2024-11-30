
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_tank, curr_tank = 0, 0
        start_station = 0
        
        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            curr_tank += gas[i] - cost[i]
            
            # If the current tank is negative, reset starting station
            if curr_tank < 0:
                start_station = i + 1
                curr_tank = 0
        
        # If total gas is sufficient, return start_station; otherwise, return -1
        return start_station if total_tank >= 0 else -1

