class Solution:
    def partition(self, s: str) -> list[list[str]]:
        res = []
        path = []

        
        def isPali(l, r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
            return True

        def backtrack(i):
            if i >= len(s):
                res.append(path[:])
                return
            
            for j in range(i, len(s)):
             
                if isPali(i, j):
                    path.append(s[i:j+1])
                    backtrack(j + 1)
                    path.pop()

        backtrack(0)
        return res