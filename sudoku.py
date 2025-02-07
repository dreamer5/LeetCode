class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        #check rows and columns
        for i in range(9):
            check_nums_h=[1,1,1,1,1,1,1,1,1] #alowed 1 to 9 in row
            check_nums_v=[1,1,1,1,1,1,1,1,1] #alowed 1 to 9 in column
            for item in board[i]:
                if item!=".":
                    item=ord(item)-49
                    if(check_nums_h[item]==0): #already seen in row
                        print("in col")
                        return False
                    check_nums_h[item]-=1
            for j in range(9):
                if board[j][i]!=".":
                    item=ord(board[j][i])-49 #unicode to number
                    if(check_nums_v[item]==0): #already seen in the column
                        print("in row")
                        return False
                    check_nums_v[item]-=1
              
        #check squares
        for square in range(9):
            check_num_sq=[1,1,1,1,1,1,1,1,1]
            add=[[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]
            cur_v,cur_h= add[square] 
            for t in range(3):
                for p in range(3):
                    if board[t+cur_v][p+cur_h]!=".":
                        item=ord(board[t+cur_v][p+cur_h])-49
                        if(check_num_sq[item]==0):
                            
                            return False
                        check_num_sq[item]-=1
    
        return True

                