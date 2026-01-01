# you are given an integer array nums and an integer k.
# In one operation, you can pick two numbers from the array whose sum equals k and remove them from the array.
# Return the maximum number of operations you can perform on the array.
# Example 1:
# Input: nums = [1,2,3,4], k = 5
# Output: 2
# Explanation: Starting with nums = [1,2,3,4]:
# - Remove numbers 1 and 4, then nums = [2,3]
# - Remove numbers 2 and 3, then nums = []
# There are no more pairs that sum up to 5, hence a total of 2 operations.
from collections import defaultdict, List

class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        # sorted_nums = nums.sort()
        # left = 0
        # right = len(nums) - 1
        # counter = 0
        # while left < right:
        #     sum = nums[left] + nums[right]
        #     if(sum == k):
        #         counter += 1
        #         left += 1
        #         right -= 1
        #     elif sum > k:
        #         right -= 1
        #     else:
        #         left += 1

        # return counter
        needSet = defaultdict(int)
        res = 0
        for n in nums:
            if needSet[n]:
                needSet[n] -= 1
                res += 1
            else:
                needSet[k-n] += 1
        return res