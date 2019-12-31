class Board:

    def printBoard(val):
        matrix = []
        for i in range(0,9):
            if(i==3 or i==6):
                matrix.append("---------")
            matrix.append(val[i*9:i*9+9])
        for i in range(0,11):
            s = matrix[i]
            matrix[i] = s[:3]+"|"+s[3:6]+"|"+s[6:]
        print("\n".join(matrix))

    def popBucket(quads,rows,columns,zeros):
        for x in zeros:
            quads[x.quad].append(x)
            rows[x.row].append(x)
            columns[x.column].append(x)

    def updatePossible(quads, rows, columns, zeros, filled):
        for x in filled:
            for n in rows[x.row]:
                if x.value in n.possible:
                    n.possible.remove(x.value)
