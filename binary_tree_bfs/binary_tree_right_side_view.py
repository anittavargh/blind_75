# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

class Solution(object):
    def rightSideView(self, root):
        
        def solve(root, level):
            if(root):
                if(len(res) == level):
                    res.append(root.val)
                solve(root.right, level+1)
                solve(root.left, level+1)
            return

        res = []
        level = 0
        solve(root, level)
        return res