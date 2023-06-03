from interpreter import draw
from chessPictures import *

figure1 = square.join(square.negative()).horizontalRepeat(4)
figure2 = square.negative().join(square).horizontalRepeat(4)

final_figure = figure2.up(figure1).verticalRepeat(2)

draw(final_figure)
