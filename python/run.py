def print_matrix(grid):
    #new line is \#
    matrix = []
    for i in range(0,9):
        if(i==3 or i==6):
            matrix.append("-----------")
        temp = []
        for j in range(0,9):
            if(j==3 or j==6):
                temp.append("|")
            temp.append(grid[i][j])
        matrix.append("".join(temp))
    print("\n".join(matrix))

def solve(puzzle):
    possible = [9][9][]
    for i in range(0,9):
        for j in range(0,9):
            if(puzzle[i][j] == 0):
                possible[i][j] = [1,2,3,4,5,6,7,8,9]
            else:
                possible[i][j] = 0
    print(possible)





def sudoku_solver(problem, solution):
    n = 9
    puzzle = [problem[i:i+n] for i in range(0, len(problem), n)]
    #print(chunks)
    for i in range(0,9):
        puzzle[i] = list(puzzle[i])
    #print(chunks)
    #print_matrix(puzzle)
    solve(puzzle)

def main():
    problem = "004300209005009001070060043006002087190007400050083000600000105003508690042910300,864371259325849761971265843436192587198657432257483916689734125713528694542916378"
    problem_set = problem.split(",")

    #print(problem_set)
    sudoku_solver(problem_set[0],problem_set[1])

main()
