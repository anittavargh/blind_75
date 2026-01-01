# You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.
# You can either start from the step with index 0, or the step with index 1.
# Return the minimum cost to reach the top of the floor.
# Example 1:
# Input: cost = [10,15,20]
# Output: 15
# Explanation: You will start at index 1.
# - Pay 15 and climb two steps to reach the top.
# The total cost is 15.
from typing import List
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        cost.append(0)
        
        for i in range(len(cost) - 4, -1, -1):
            cost[i] += min(cost[i+1], cost[i+2])
            
        return min(cost[0], cost[1])
    
# class Solution:
#     def minCostClimbingStairs(self, cost: List[int]) -> int:
#         # edge case
#         if len(cost) == 0:
#             return 0
#         if len(cost) == 1:
#             return cost[0]
#         dp = [0] * (len(cost)+1) # dp[-1] denotes the top
#         # dp[i] = minimum cost of reaching index i
#         dp[0], dp[1] = 0, 0 # no cost
        
#         for i in range(2, len(dp)):
#             dp[i] = min(dp[i-2] + cost[i-2], cost[i-1] + dp[i-1])

#         return dp[-1]
