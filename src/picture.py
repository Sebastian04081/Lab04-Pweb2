from colors import *
class Picture:
  def __init__(self, img):
    self.img = img;

  def __eq__(self, other):
    return self.img == other.img

  def _invColor(self, color):
    if color not in inverter:
      return color
    return inverter[color]

  def verticalMirror(self):
    """ Devuelve el espejo vertical de la imagen """
    vertical = []
    for value in self.img:
    	vertical.append(value[::-1])
    return vertical

  def horizontalMirror(self):
    """ Devuelve el espejo horizontal de la imagen """
    return Picture(None)

  def negative(self):
    """ Devuelve un negativo de la imagen """
    negative = []

    for row in self.img:
        neg_row = ""
        for pixel in row:
            neg_row += self._invColor(pixel)
        negative.append(neg_row)

    return Picture(negative)

  def join(self, p):
    """ Devuelve una nueva figura poniendo la figura del argumento 
        al lado derecho de la figura actual """
    join = []

    for i in range(len(self.img)):
        join.append(self.img[i] + p.img[i])

    return Picture(join)

  def up(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la 
        figura actual """
    return Picture(None)

  def under(self, p):
    """ Devuelve una nueva figura poniendo la figura p sobre la
        figura actual """
    return Picture(None)
  
  def horizontalRepeat(self, n):
    """ Devuelve una nueva figura repitiendo la figura actual al costado
        la cantidad de veces que indique el valor de n """
    return Picture(None)

  def verticalRepeat(self, n):
    """ Devuelve una nueva figura que repite verticalmente la imagen actual 
        del objeto n veces """
    return Picture(None)

  # Extra: Sólo para realmente viciosos 
  def rotate(self):
    """ Devuelve una figura rotada en 90 grados, puede ser en sentido horario
    o antihorario """
    return Picture(None)

