class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        # Represents the tank
        tank = 0

        # base case
        if sum(gas) < sum(cost):
            return -1
        
        # Start at any i
        # Keep finding tank+= gas[i]-cost[i]
        # if tank<=0 then reset tank = 0 and move to start = i+1
    
        start = 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                tank = 0
                
        return start