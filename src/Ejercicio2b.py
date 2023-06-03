from interpreter import draw
from chessPictures import *

draw(knight.negative().verticalMirror().join(knight.verticalMirror()).up(knight.join(knight.negative())))
