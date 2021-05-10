def CheckRow(Matrix, x, value):
    for i in range(9):
        if (Matrix[x][i] == value):
            return False
    return True
def CheckColumn(Matrix, y, value):
    for i in range(9):
        if (Matrix[i][y] == value):
            return False
    return True
def CheckSquad(Matrix, x, y, value):
    for i in range(x//3 * 3, x//3 * 3 + 3):
        for j in range(y//3 * 3, y//3 * 3 + 3):
            if (Matrix[i][j] == value):
                return False
    return True
def find_empty(Matrix):
    for i in range(9):
        for j in range(9):
            if Matrix[i][j] == 0:
                return (i, j)  
    return None
def CheckPrint(Matrix):
    Check = True
    for i in range(9):
        if Check == False:
            break
        for j in range(9):
            if (Matrix[i][j] < 1) | (Matrix[i][j] > 9):
                Check = False
                break
            for k in range(1, 10):
                if CheckRow(Matrix, i, k) | CheckColumn(Matrix, i, k) | CheckRow(Matrix, i, k):
                    Check = False
                    break
    return Check
def PrintSolution(Matrix):
    if (CheckPrint(Matrix) == 0):
        print(-1)
    else:
        for i in Matrix:
            for j in i:
                print(j, end = " ")
            print()
    
def Sudoku(Matrix):
    find = find_empty(Matrix)
    if not find:
        return True
    else:
        row, col = find
    for i in range(1,10):
        if CheckRow(Matrix, row, i) & CheckColumn(Matrix, col, i) & CheckSquad(Matrix, row, col, i):
            Matrix[row][col] = i
            if Sudoku(Matrix):
                return True
            Matrix[row][col] = 0
    return False
Matrix = []
for i in range(9):   
    T = []
    for j in input().strip().split():
        T.append(int(j))
    Matrix.append(T)

if (Sudoku(Matrix) == 0):
    print(-1)
else:
    PrintSolution(Matrix)