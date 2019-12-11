class Tile:
    def getQuad(row, column):
        quad = (column-1)/3 + 1
        quad += ((row-1)/3) * 3
        return quad
        
    def __init__(self, value, possible, pos):

        self.value = value
        self.possible = possible
        self.row = pos/9 + 1
        self.column = pos%9 + 1
        self.quad = getQuad(row, column)

    ##
    ## 1|2|3 1-9
    ## 4|5|6
    ## 7|8|9
    ##
    def getQuad(row, column):
        quad = (column-1)/3 + 1
        quad += ((row-1)/3) * 3
        return quad
