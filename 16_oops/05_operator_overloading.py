class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def sum(self, p):
        return Point((self.x + p.x), (self.y + p.y))

    def print_point(self):
        print(f"x is {self.x} and y is {self.y}")

    def __add__(self, p):
        return Point((self.x + p.x), (self.y + p.y))


p1 = Point(2, 3)
p2 = Point(4, 5)

# p = p1.sum(p2)
p = p1 + p2  # We overloaded the + operator by writting __add__ method

"""
__sub__ (-), __mul__ (*), __truediv__ (/), __eq__ (==), __ne__ (!=), __lt__ (<), __gt__ (>), __len__ (len()), __getitem__, __setitem__, __delitem__ (for list/dictionary-like behavior – allowing you to use [] with your objects).
"""

p.print_point()
