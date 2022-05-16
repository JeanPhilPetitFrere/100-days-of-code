#Why use classes —> 1. Safe from bugs 2. Easy to understand 3. Ready for change
import turtle #kite copilot
class Polygon:
    def __init__(self,sides,name,size=100,color='red'):
        self.sides = sides
        self.name = name
        self.size = size
        self.color = color
        self.interior_angles = (self.sides-2)*180
        self.angle = self.interior_angles/self.sides
    
    def draw(self):
        turtle.color(self.color)
        for i in range(self.sides):
            turtle.forward(self.size)
            turtle.right(180 - self.angle)
            
        #turtle.done()
        #overloading operators

class Square(Polygon):
    def __init__(self,size=100,color='red'):
        super().__init__(4,'square',size,color)
    
    def draw(self):
        turtle.begin_fill()
        super().draw()
        turtle.end_fill()

square = Square()
print(square.sides)



#square = Polygon(4,'Square')
pentagon = Polygon(5, 'Pentagon')

print(square.sides)
print(pentagon.name)
print(square.interior_angles)
print(pentagon.angle)


hexagon =  Polygon(6, 'Hexagon')
square.draw()

#self is 