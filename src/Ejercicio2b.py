from interpreter import draw
from chessPictures import *

negative = knight.negative()
draw(negative.verticalMirror().join(knight.verticalMirror()).up(knight.join(negative))
