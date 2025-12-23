# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# Input: root = [1,2,3,null,5,null,4]
# Output: [1,3,4]

from typing import deque
#bfs solutionfrom collections import deque

class Solution:
    def rightSideView(self, root):
        if not root:
            return []
        res, q = [], deque([root])

        while q:
            size = len(q)
            for i in range(size):
                node = q.popleft()
                if i == size - 1:
                    res.append(node.val) # append last node of the level
                # push children
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res

#dfs solution
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