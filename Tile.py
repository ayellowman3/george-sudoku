import math

class Tile:

    def __init__(self, value, possible, row, col, quad):

        self.value = value
        self.possible = possible
        self.row = row
        self.col = col
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

    def setValue(value):
        value = value

    def rmPossible(num):
        for i in possible:
            if(i == num):
                possible.remove(num)

    def clearPossible():
        possible = []
