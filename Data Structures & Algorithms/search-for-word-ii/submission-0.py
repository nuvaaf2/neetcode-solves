class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = {}
        for word in words:
            curr = trie
            for char in word:
                if char not in curr:
                    curr[char] = {}
                curr = curr[char]
            curr['#'] = word

        ROWS, COLS = len(board), len(board[0])
        res = set()

        def dfs(r, c, node):
            if r < 0 or c < 0 or r >= ROWS or c >= COLS or board[r][c] == '@':
                return
            char = board[r][c]

            if char not in node:
                return

            next_node = node[char]

            if '#' in next_node:
                res.add(next_node['#'])

            board[r][c] = '@'

            dfs(r + 1, c, next_node)
            dfs(r - 1, c, next_node)
            dfs(r, c + 1, next_node)
            dfs(r, c - 1, next_node)

            board[r][c] = char


        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, trie)

        return list(res)





        