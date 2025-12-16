class Solution(object):
    def removeStars(self, s):
        stack = []
        for i in s:
            if i == "*" and stack:
                stack.pop()
            else:
                stack.append(i)
        return "".join(stack)
    
sol = Solution()
result = sol.removeStars("leet**cod*e")
print(result)
    