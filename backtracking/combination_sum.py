# Find all valid combinations of k numbers that sum up to n such that the following conditions are true:
# Only numbers 1 through 9 are used.
# Each number is used at most once.
# Return a list of all possible valid combinations. The list must not contain the same combination twice, and the combinations may be returned in any order.
# Example 1:
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Explanation:
# 1 + 2 + 4 = 7
from typing import List

class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(start, path, target, k):
            if target == 0 and k == 0:
                res.append(path[:])
                return 

            for i in range(start, 10):
                if i > target or k <= 0:
                    break
                path.append(i)
                backtrack(i+1, path, target - i, k - 1)
                path.pop()
        
        res = []
        path = []
        start = 1
        backtrack(start, path, n,  k)
        return res
        