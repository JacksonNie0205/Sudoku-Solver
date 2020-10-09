import copy
class sudoku:
    def __init__(self, board):
        self.row_nums = dict()
        self.col_nums = dict()
        self.section_nums = dict()

        if not self.is_valid_board(board):
            raise ValueError("The board to solve is not valid, please modify the board and try again!")
        print("\nThe board to solve is: ")
        self.print_board(board)

    def print_board(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if col != 8:
                    print(board[row][col], end=" ")
                elif col == 8:
                    print(board[row][col])
                if col == 2 or col == 5:
                    print("|", end=" ")

            if(row == 2 or row == 5):
                print("---------------------") 

    #check if cell has no number
    def is_empty(self, board, row, col):
        if(board[row][col] == 0):
            return True
        else:
            return False
    #return list of all cells that have no number
    def all_empty_cells(self, board):
        empty_cells = []
        for row in range(len(board)):
            for col in range(len(board)):
                if board[row][col] == 0:
                    empty_cells.append((row, col))
        return empty_cells
    
    def contains_duplicate(self, nums):

        return len(nums) != len(set(nums))
    #returns which section the (row,col) is in
    def get_section(self, row, col):
        if row <= 2 and col <=2:
            return 0
        elif row <= 2 and col <= 5:
            return 1
        elif row <=2 and col <= 8:
            return 2
        elif row <= 5 and col <= 2:
            return 3
        elif row <= 5 and col <= 5:
            return 4
        elif row <= 5 and col <= 8:
            return 5
        elif row <= 8 and col <= 2:
            return 6
        elif row <= 8 and col <= 5:
            return 7
        elif row <= 8 and col <= 8:
            return 8
    
    def is_valid_board(self, board):
        self.row_nums.clear()
        self.col_nums.clear()
        self.section_nums.clear()
        for row in range(len(board)):
            for col in range(len(board[row])):
                if type(board[row][col]) != int or board[row][col] > 9 or board[row][col] < 0:
                    return False
                if row not in self.row_nums.keys():
                    self.row_nums[row] = list()
                    if board[row][col] != 0:
                        self.row_nums[row].append(board[row][col])
                else:
                    if board[row][col] != 0:
                        self.row_nums[row].append(board[row][col])
                    if self.contains_duplicate(self.row_nums[row]):
                        return False
                if col not in self.col_nums.keys():
                    self.col_nums[col] = list()
                    if board[row][col] != 0:
                        self.col_nums[col].append(board[row][col])
                else:
                    if board[row][col] != 0:
                        self.col_nums[col].append(board[row][col])
                    if self.contains_duplicate(self.col_nums[col]):
                        return False
                if self.get_section(row,col) not in self.section_nums.keys():
                    self.section_nums[self.get_section(row,col)] = list()
                    if board[row][col] != 0:
                        self.section_nums[self.get_section(row,col)].append(board[row][col])
                else:
                    if board[row][col] != 0:
                        self.section_nums[self.get_section(row,col)].append(board[row][col])
                    if self.contains_duplicate(self.section_nums[self.get_section(row,col)]):
                        return False
        return True
    
    def find_empty_cell(self, board):
        for row in range(len(board)):
            for col in range(len(board[row])):
                if self.is_empty(board,row,col):
                    return row,col
        return -1,-1




      
    def is_valid_insert(self, board, row, col, num):
        # b = copy.copy(board)
        # b[row][col] = num
        # if self.is_valid_board(b):
            
        #     return True
        # else:
            
        #     return False

        #check row
        for i in range(0,9):
            if board[row][i] == num and i != col:
                return False
        
        #check col
        for j in range(0,9):
            if board[j][col] == num and j != row:
                return False
        
        #check section box
        section = self.get_section(row, col)
        if section == 0:
            for r in range(0,3):
                for c in range(0,3):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 1:
            for r in range(0,3):
                for c in range(3,6):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 2:
            for r in range(0,3):
                for c in range(6,9):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 3:
            for r in range(3,6):
                for c in range(0,3):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 4:
            for r in range(3,6):
                for c in range(3,6):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 5:
            for r in range(3,6):
                for c in range(6,9):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 6:
            for r in range(6,9):
                for c in range(0,3):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 7:
            for r in range(6,9):
                for c in range(3,6):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        if section == 8:
            for r in range(6, 9):
                for c in range(6,9):
                    if board[r][c] == num and (r, c) != (row, col):
                        return False
        
        return True
    
    def solve_sudoku(self, board):
        row, col = self.find_empty_cell(board)
        
        if row == -1 and col == -1:
            return True
        else:
            for num in range(1,10):
                if self.is_valid_insert(board, row, col, num):
                    board[row][col] = num

                    if self.solve_sudoku(board):
                        return True
                    
                board[row][col] = 0
            
            return False
   
    @staticmethod
    def get_board():
        board = list()
        wrong_type = False
        i = 0
       
        while i < 9:
            if wrong_type:
                i = i - 1
            wrong_type = False
            board.append([])
            row = input("Please enter row %s of the sudoku, enter 0 for empty cells: "%(i+1))
            while(len(row) != 9):
                print("The length of the row is not correct, should be 9 digits.")
                row = input("Please enter row %s of the sudoku, enter 0 for empty cells: "%(i+1))
            for k in range(len(row)):
                if not row[k].isnumeric():
                    print("Row elements need to be integer numbers.")
                    wrong_type = True
                    break
                else:
                    board[i].append(int(row[k]))
            i += 1
        
        return board


def main():
    board = sudoku.get_board()
    s = sudoku(board)
    print("\nSolving...")
    s.solve_sudoku(board)
    print("\nSolved!!")
    s.print_board(board)
main()