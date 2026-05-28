class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        
        def dfs(node, max_val):

            if not node:
                return 0

            
            if node.val >= max_val:
                res = 1
                max_val = node.val
            else:
                res = 0

            res += dfs(node.left, max_val)
            res += dfs(node.right, max_val)

            return res

        return dfs(root,root.val)

        