import math

class Tile:

    def __init__(self, value, possible, row, column, quad):

        self.value = value
        self.possible = possible
        self.row = row
        self.column = column
        self.quad = quad

    ##
    ## 1|2|3 1-9
    ## 4|5|6
    ## 7|8|9
    ##
    def getRow(val):
        return (math.floor(val/9 + 1))

    def getColumn(val):
        return val%9 + 1

    def getQuad(row, column):
        x = math.floor((column-1)/3 + 1)
        x += (math.floor((row-1)/3) * 3)
        return x
