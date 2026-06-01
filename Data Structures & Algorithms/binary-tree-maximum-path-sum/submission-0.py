class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        res = [root.val]

        def dfs(node):
            if not node:
                return 0

            left_max = max(0, dfs(node.left))
            right_max = max(0, dfs(node.right))

            current_split_sum = node.val + left_max + right_max
            res[0] = max(res[0], current_split_sum)

            return node.val + max(left_max, right_max)

        dfs(root)

        return res[0]

        