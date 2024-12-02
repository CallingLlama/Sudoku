from graphics import *


class SudokuBox:
   def __init__(self, width, height, xCoord, yCoord, number):
       self.width = width
       self.height = height
       self.x = xCoord
       self.y = yCoord
       self.number = number
       if self.number == " ":
           self.editable = True
       else:
           self.editable = False


   def getNumber(self):
       return self.number


   def setNumber(self, num):
       self.number = num


   def canEdit(self):
       return self.editable


   def drawBox(self, window):
       box = Rectangle(Point(self.x, self.y), Point(self.x + self.width, self.y + self.height))
       num = Text(Point(self.x + (self.width / 2), self.y + (self.height / 2)), self.number)
       box.draw(window)
       num.draw(window)
