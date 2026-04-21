from collections import defaultdict

class Solution:
    def isValidSudoku(self, board):
        rows  = defaultdict(set)
        cols  = defaultdict(set)
        boxes = defaultdict(set)
        
        for i in range(9):
            for j in range(9):
                if board[i][j] == ".":    
                    continue
                num = board[i][j]
                box = (i//3, j//3)
                if num in rows[i] or num in cols[j] or num in boxes[box]:
                    return False
                rows[i].add(num)          
                cols[j].add(num)         
                boxes[box].add(num)       
        return True