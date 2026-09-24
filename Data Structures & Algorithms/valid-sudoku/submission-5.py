class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        # duplicates -> set (add func), hash
        rows = defaultdict(set)
        cols = defaultdict(set)
        squares = defaultdict(set)  
        # idx 0, 0: the first 3x3 squares [row: 0-2, cols:0-2] (top left)
        # idx 1, 0: the middle 3x3 squares [row:3-5, cols:0-2] (left middle)


        for r in range(9):
            for c in range(9):
                # 1. if '.' then skip
                if board[r][c] == ".":
                    continue
                # 2. False conditions
                if (board[r][c] in rows[r] or board[r][c] in cols[c] or board[r][c] in squares[(r//3), (c//3)]):
                    return False 

                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[(r//3), (c//3)].add(board[r][c])

        return True

        