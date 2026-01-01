# You are given two positive integer arrays spells and potions, of length n and m respectively, where spells[i] represents the strength of the ith spell and potions[j] represents the strength of the jth potion.
# You are also given an integer success. A spell and potion pair is considered successful if the product of their strengths is at least success.
# Return an integer array pairs of length n where pairs[i] is the number of potions that will form a successful pair with the ith spell.
# Example 1:
# Input: spells = [5,1,3], potions = [1,2,3,4,5], success = 7
# Output: [4,0,3]
from typing import List

class Solution:

    def valid_potions(self, spell, success, potions):
            potions_needed = ((success + spell - 1)) // spell
            l, r = 0, len(potions)
            while l < r:
                mid = l + (r-l)//2
                if(potions[mid] >= potions_needed):
                    r = mid
                else:
                    l = mid + 1
            return l

    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        potions.sort()
        res = []
        for i in range(len(spells)):
            res.append(len(potions) - self.valid_potions(spells[i], success, potions))
        return res