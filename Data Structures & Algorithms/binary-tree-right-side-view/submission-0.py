from collections import deque
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        res = []
        if not root:
            return res
        q = deque([root])
        while q:
            rightSide = None
            level_size = len(q)

            for i in range(level_size):
                node = q.popleft()

                if node:
                    rightSide = node

                    if node.left:
                        q.append(node.left)

                    if node.right:
                        q.append(node.right)

            if rightSide:
                res.append(rightSide.val)

        return res


        