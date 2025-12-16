# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def searchBST(self, root, val):
        if(root and val == root.val):
            return root
        if(root and val > root.val):
            return self.searchBST(root.right, val)
        if(root and val < root.val):
            return self.searchBST(root.left, val)
        else:
            return None

