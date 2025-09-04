class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1
        
        current_gas = 0
        start_index = 0
        
        for i in range(len(gas)):
            current_gas += gas[i] - cost[i]
            
            if current_gas < 0:
                current_gas = 0
                start_index = i + 1
        
        return start_index
