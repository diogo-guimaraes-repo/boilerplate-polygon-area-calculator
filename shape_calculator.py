class Rectangle:

  def __init__(self, width, height):
    self.width = width
    self.height = height

  def __str__(self):
    ret = "Rectangle(width=" + str(self.width) + ", height="+ str(self.height) + ")"
    return ret

  def set_width(self, width):
    self.width = width

  def set_height(self, height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return 2*self.width + 2*self.height

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    pic = ""
    if self.width <= 50 and self.height <= 50:
      
      for i in range(self.height):
        for j in range(self.width):
          pic += "*"
          if j == self.width-1:
            pic += "\n"
    else:
      pic = "Too big for picture."

    return pic

  def get_amount_inside(self, rectangle):
    return self.get_area() // rectangle.get_area()

class Square(Rectangle):
  
  def __init__(self, length):
    self.set_side(length)

  def __str__(self):
    ret = "Square(side=" + str(self.width) + ")"
    return ret

  def set_side(self, length):
    self.width = length
    self.height = length

  def set_width(self, width):
    self.set_side(width)

  def set_height(self, height):
    self.set_side(height)
