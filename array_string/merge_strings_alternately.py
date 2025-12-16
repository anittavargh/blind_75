class Solution(object):
    def mergeAlternately(self, word1, word2):
        result = ""
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0

        while i < m or j < n: 
            if i < m:
                result += word1[i]
                i+=1
            if j < n:
                result += word2[j]
                j +=1
        return result
    

word1 = input("Enter first word: ")
word2 = input("Enter second word: ")

sol = Solution()
print(sol.mergeAlternately(word1, word2))
    


