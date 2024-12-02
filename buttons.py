from operator import truediv
from graphics import *


class Button:

    def __init__(self, win, center, width, height, label):
        # Calculating the half of the width and height to calculate the points to define the rectangle (Bottom left & top right)
        w, h = width/2, height/2
        x, y = center.getX(), center.getY()
        self.xmax, self.xmin = x+w, x-w
        self.ymax, self.ymin = y+h, y-h
        # Creating the point that will help define the rectangle
        p1 = Point(self.xmin, self.ymin)
        p2 = Point(self.xmax, self.ymax)

        self.rect = Rectangle(p1, p2)
        self.rect.setFill("lightgray")
        self.rect.draw(win)
        self.label = Text(center, label)
        self.label.draw(win)
        self.deactivate()

    def clicked(self, p):
        insideX = self.xmin <= p.getX() and p.getX() <= self.xmax
        insideY = self.ymin <= p.getY() and p.getY() <= self.ymax

        return self.active and insideX and insideY

    def getLabel(self):
        return self.label.getText()

    def activate(self):
        self.label.setFill("black")
        self.rect.setWidth(2)
        self.active = True

    def deactivate(self):
        self.label.setFill("black")
        self.rect.setWidth(1)
        self.active = False