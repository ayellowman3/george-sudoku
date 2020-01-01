from math import floor
from Tile import Tile
import csv
import pandas as pd
import time


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
    #print(input)
    #print(problem_set)
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
            #dBoard(filled, zeros)
            #print(solution)
            return False
        update_possible(zeros, pRow, pCol, pQuad)
    #dBoard(filled, zeros)
    #print(solution)
    return True




    #solve(puzzle)

def main():

    #up to 45 files
    numFiles = 45
    files = []
    for i in range(1,numFiles+1):
        files.append('sudoku' + str(i) + '.csv')
    #files = ['sample.csv']

    line_count = 0
    correct = 0
    incorrect_count = 0
    result = []
    for i in files:
        start_time = time.time()
        incorrect = []
        with open('sudoku/'+i) as csv_file:
            csv_reader = csv.reader(csv_file)
            for row in csv_reader:
                problem = ','.join(row)
                if(sudoku_solver(problem)==False):
                    incorrect.append(problem)
        line_count += 200000
        incorrect_count += len(incorrect)
        correct = line_count-incorrect_count
        print(str(correct)+' out of '+str(line_count)+' correct')
        result.append(str(200000-len(incorrect))+' out of 200,000 correct')
        print("--- %s seconds ---" % (time.time() - start_time))
        df = pd.DataFrame(incorrect, columns=["dataset"])
        df.to_csv('incorrect/'+i, index=False, header=False)
    df = pd.DataFrame(list(zip(files, result)), columns=["files","results"])
    df.to_csv('result.csv', index=False, header=False)


main()
