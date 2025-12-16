class Solution(object):
    def mergeZeroes(self, nums):
        i = 0
        for j in range(len(nums)):
                if(nums[j] != 0):
                    nums[i], nums[j] = nums[j], nums[i]
                    i +=1
        return nums 
            
inputArray = list(map(int, input("Enter array: ").split()))
sol = Solution()
print(sol.mergeZeroes(inputArray))