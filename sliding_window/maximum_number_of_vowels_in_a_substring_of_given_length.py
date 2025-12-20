class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = "aeiouAEIOU"
        count = 0
        left = 0
        max_count = 0
        for i in range(k):
            if s[i] in vowels:
                count +=1
        max_count = max(count, max_count)

        for i in range(k, len(s)):
            if s[left] in vowels:
                count = count - 1
                left = left + 1
            else:
                left = left + 1

            if(s[i] in vowels):
                count +=1   
            max_count = max(count, max_count)
        
        return max_count
            