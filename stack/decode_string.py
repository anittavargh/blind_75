class Solution:
    def decodeString(self, s: str) -> str:

        stack = []
        curr_string = ""
        curr_num = 0
        
        for i in s:
            if i == "[":
                stack.append(curr_num)
                stack.append(curr_string)
                curr_string = ""
                curr_num = 0
            elif i == "]":
                prev_string = stack.pop()
                num = stack.pop()
                curr_string = prev_string + num*curr_string
            elif i.isalpha():
                curr_string += i
            else:
                curr_num = curr_num*10 + int(i)

        return curr_string
                