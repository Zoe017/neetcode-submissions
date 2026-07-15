# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        res = True
        def helper(root):
            nonlocal res
            if not root:
                return 0
            righth = helper(root.right) + 1
            lefth = helper(root.left) + 1
            if righth - lefth < -1 or righth -lefth > 1:
                res = False
            return max(righth,lefth)
        helper(root)
        return res