# Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.
# Example 1:
# Input: arr = [1,2,2,1,1,3]
# Output: true
# Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.

from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        unique = {}

        for i in range(len(arr)):
            if arr[i] not in unique:
                unique[arr[i]] = 1
            else:
               unique[arr[i]] = unique.get(arr[i], 0) + 1
        print(unique)
        
        #find max_key
        #max_key = max(unique, key=unique.get)
        # print(max_key)
        seen = set()
        uniqueV = True

        for v in unique.values():
            if v in seen:
                uniqueV = False
                break
            seen.add(v)

        return uniqueV

            
        