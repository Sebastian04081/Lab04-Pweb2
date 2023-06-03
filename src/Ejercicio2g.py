from interpreter import draw
from chessPictures import *

def buildSquare(piece, x):
    if x == 0:
        return square.negative().under(piece)
    if x == 1:
        return square.under(piece)
    return None

def buildPawns():
    figure = buildSquare(pawn, 1)
    for i in range(7):
        if i % 2 == 0:
            figure = figure.join(buildSquare(pawn, 0))
        else:
            figure = figure.join(buildSquare(pawn, 1))
    return figure

def buildMain():
    figure = buildSquare(rock, 0)
    figure = figure.join(buildSquare(knight, 1))
    figure = figure.join(buildSquare(bishop, 0))
    figure = figure.join(buildSquare(queen, 1))
    figure = figure.join(buildSquare(king, 0))
    figure = figure.join(buildSquare(bishop, 1))
    figure = figure.join(buildSquare(knight, 0))
    figure = figure.join(buildSquare(rock, 1))

    return figure

# Building Rows
whitePawns = buildPawns()
mainWhite = buildMain()

# Building empty squares
squaresRow = square.join(square.negative()).horizontalRepeat(4)
invertedSquaresRow = squaresRow.verticalMirror()
emptySquares = invertedSquaresRow.up(squaresRow).verticalRepeat(2)

# Building formations
whiteTroop = mainWhite.up(whitePawns)
blackTroop = whitePawns.negative().up(mainWhite.negative())

# Building the chessboard
chessboard = whiteTroop.up(emptySquares).up(blackTroop)

draw(chessboard)

