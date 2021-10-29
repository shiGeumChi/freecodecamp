class Rectangle:
  def __init__(self,width,height):
    self.width = width
    self.height = height


  def __repr__(self):
    s = f"Rectangle(width={self.width}, height={self.height})"
    return s


  def set_width(self,width):
    self.width = width

  def set_height(self,height):
    self.height = height

  def get_area(self):
    return self.width * self.height

  def get_perimeter(self):
    return self.width * 2 + self.height * 2

  def get_diagonal(self):
    return (self.width ** 2 + self.height ** 2) ** .5

  def get_picture(self):
    if( self.width >=50 | self.height >=50):
      return "Too big for picture."
    s =""
    for i in range(0,self.height):
      for j in range(0,self.width):
        s += "*"
      s+="\n"
    return s

  def get_amount_inside(self,instance):
    return int((self.width / instance.width) * (self.height / instance.height))




class Square(Rectangle):
  def __init__(self,side):
    self.width = side
    self.height = side

  def set_side(self,side):
    self.width = side
    self.height = side

  def __repr__(self):
    return f'Square(side={self.width})'

  def set_width(self,side):
    self.width = side
    self.height = side

  def set_height(self,side):
    self.width = side
    self.height = side



rect = Rectangle(10, 5)
print(rect.get_area())
rect.set_height(3)
print(rect.get_perimeter())
print(rect)
print(rect.get_picture())

sq = Square(9)
print(sq.get_area())
sq.set_side(4)
print(sq.get_diagonal())
print(sq)
print(sq.get_picture())

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))