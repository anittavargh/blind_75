from typing import List 
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxVal = max(candies)
        result = []

        for i in candies:
            if i + extraCandies >= maxVal:
                result.append(True)
            else:
                result.append(False)
        return result
        