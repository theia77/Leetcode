class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
    
        for i in range(9):
            d={}
            for j in range(9):
                if board[i][j]!='.':
                    if board[i][j] in d:
                        return False
                    else:
                        d[board[i][j]]=1
        
        for k in range(9):
            d1={}
            for f in range(9):
                if board[f][k]!='.':
                    if board[f][k] in d1:
                        return False
                    else:
                        d1[board[f][k]]=1
        for start_row in range(0, 9, 3):       
            for start_col in range(0, 9, 3):   
                d2={}
                for a in range(start_row,start_row+3):
                    for b in range(start_col,start_col+3):
                        if board[a][b]!='.':
                            if board[a][b] in d2:
                                return False
                            else:
                                d2[board[a][b]]=1
        return True
