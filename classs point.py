import math

class point:
    x = 0
    y = 0

    def _init_(self, a, b):
        self.x = a
        self.y = b
    
    def translate(self, dx, dy):
        self.x += dx
        self.y += dy  

    def distance(self, x1, y1):
        d = math.sqrt((self.x - x1)**2+(self.y - y1)**2)
        return d
        
    def distance_from_origin(self):
        d = math.sqrt(self.x**2 + self.y**2)
        return d
        
def main():
    p1 = point(2,-5)
    p2 = point(3,9)
    
    print(p1.x)
    print(p1.y)
    print(p2.x)
    print(p2.y)

    p1.translate(-5, 7)
    print(p1.x)
    print(p1.y)

    print(p1.distance(10,10))
    print(p1.distance_from_origin())
