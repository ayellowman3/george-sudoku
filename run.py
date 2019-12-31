from math import floor
from Tile import Tile
import csv


def dBoard(filled, zeros):
    board = ['0']*81
    for t in filled:
        index = t.col + 9*t.row
        board[index] = str(t.value)
    print(''.join(board))

def update_possible(zeros, pRow, pCol, pQuad):
    for z in zeros:
        possible = []
        for i in range(1,10):
            if(pRow[z.row][i]==True and pCol[z.col][i]==True and pQuad[z.quad][i]==True):
                possible.append(i)
        z.possible = possible
        #print(z.possible)
    return zeros

def sudoku_solver(input):
    problem_set = input.split(",")
    problem = problem_set[0]
    solution = problem_set[1]

    zeros = []
    filled = []
    pRow = []
    pCol = []
    pQuad = []
    for i in range(9):
        pRow.append([True,True,True,True,True,True,True,True,True,True])
        pCol.append([True,True,True,True,True,True,True,True,True,True])
        pQuad.append([True,True,True,True,True,True,True,True,True,True])

    for i in range(len(problem)):
        row = int(i/9)
        col = int(i%9)
        quad = int(col/3) + 3*int(row/3)


        #print(str(i)+" "+str(row)+" "+str(col)+" "+str(quad))
        #print(3*floor(row/3))
        if(int(problem[i])==0):
            zeros.append(Tile(0, [], row, col, quad))
        else:
            t = Tile(int(problem[i]), [], row, col, quad)
            filled.append(t)
            pRow[t.row][t.value] = False
            pCol[t.col][t.value] = False
            pQuad[t.quad][t.value] = False

        #print(len(zeros))
        #print(len(filled))
    update_possible(zeros, pRow, pCol, pQuad)
    while(len(zeros)>0):
        zLen = len(zeros)
        for z in zeros:
            #print(z.possible)
            if(len(z.possible) == 1):
               #print("single")
                z.value = z.possible[0]
                pRow[z.row][z.value] = False
                pCol[z.col][z.value] = False
                pQuad[z.quad][z.value] = False
                filled.append(z)
                zeros.remove(z)
        if(zLen == len(zeros)):
            dBoard(filled, zeros)
            print(solution)
            return False
        update_possible(zeros, pRow, pCol, pQuad)
    #dBoard(filled, zeros)
    #print(solution)
    return True




    #solve(puzzle)

def main():
    #problem = "004300209005009001070060043006002087190007400050083000600000105003508690042910300,864371259325849761971265843436192587198657432257483916689734125713528694542916378"


    #print(problem_set)
    #print(sudoku_solver(problem))

    files = ['sudoku1.csv','sudoku2.csv','sudoku3.csv','sudoku4.csv','sudoku5.csv',]
    line_count = 0
    correct = 0
    incorrect = []
    for i in files:
        with open(i) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                if(sudoku_solver(','.join(row))):
                    correct += 1
                else:
                    incorrect.append(row)
                line_count += 1
            #print(line_count)
            print(str(correct)+' out of '+str(line_count)+' correct')


main()
