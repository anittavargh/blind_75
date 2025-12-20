class Solution(object):
    def largestAltitude(self, gain):
        highest = 0
        altitude = 0
        for i in gain:
            altitude += i
            highest = max(altitude, highest)
        return highest
    

# class Solution:
#     def largestAltitude(self, gain: List[int]) -> int:
#         highest_alt = 0
#         new_gain =  0

#         for i in range(len(gain)):
#             temp = new_gain + gain[i]
#             new_gain = temp
#             if(temp > highest_alt):
#                 highest_alt = temp

#         return highest_alt