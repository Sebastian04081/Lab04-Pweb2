from interpreter import draw
from chessPictures import *

figure1 = square.join(square.negative()).horizontalRepeat(4)
figure2 = square.negative().join(square).horizontalRepeat(4)

draw(figure1)
# draw(figure2)
