from Tile import *

def sudoku_solver(start, finished):
    print(start)
    zeros = []
    filled = []
    for x in range(81):
        #print(x)
        if(start[x]=='0'):
            zeros.append(Tile(start[x],[1,2,3,4,5,6,7,8,9],x))
    #square = Tile(start,[1])
    print len(zeros)
    for x in zeros:
        print(str(x.value) + " " + str(x.row) + " " + str(x.column) + " " + str(x.quad))








def main():
    #first problem set
    problem = "004300209005009001070060043006002087190007400050083000600000105003508690042910300,864371259325849761971265843436192587198657432257483916689734125713528694542916378"
    problem_set = problem.split(",")

    #print(problem_set)
    sudoku_solver(problem_set[0],problem_set[1])

main()
