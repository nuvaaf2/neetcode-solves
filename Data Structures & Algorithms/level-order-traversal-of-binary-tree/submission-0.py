from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        if not root:
            return res

        q = deque([root])


        while q:
            level_size = len(q)
            current_level = []
            
            for _ in range(level_size):
                node = q.popleft()
                current_level.append(node.val)
                if node.left:
                    q.append(node.left)

                if node.right:
                    q.append(node.right)

            res.append(current_level)

        return res

