# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res
        dq = collections.deque([root])
        while dq:
            temp = []
            l = len(dq)
            for i in range(l):
                node = dq.popleft()
                if node:
                    temp.append(node.val)
                    dq.append(node.left)
                    dq.append(node.right)
            if temp:
                res.append(temp)
        return res
