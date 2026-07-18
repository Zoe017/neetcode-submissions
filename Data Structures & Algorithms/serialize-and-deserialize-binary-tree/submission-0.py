# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:
    
    # Encodes a tree to a single string.
    def serialize(self, root: Optional[TreeNode]) -> str:
        val = []
        def dfs(root):
            nonlocal val
            if not root:
                val.append("N")
            else:
                val.append(str(root.val))
                dfs(root.left)
                dfs(root.right)
        dfs(root)
        return ",".join(val)
            
    # Decodes your encoded data to tree.
    def deserialize(self, data: str) -> Optional[TreeNode]:
        val = deque(data.split(","))
        def dfs():
            v = val.popleft()
            if v == "N":
                return None
            node = TreeNode(int(v))
            node.left = dfs()
            node.right = dfs()
            return node
        return dfs()





