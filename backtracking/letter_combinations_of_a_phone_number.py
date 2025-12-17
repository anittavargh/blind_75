# Input: digits = "23"
# Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]

class Solution(object):
    def letterCombinations(self, digits):
        if not digits:
            return []

        phone = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        path = ""
        res = []

        def dfs(i, path):
            if i == len(digits):
                res.append(path)
                return
            
            for ch in phone[digits[i]]:
                dfs(i + 1, path + ch)

 
        dfs(0, path)
        return res
        