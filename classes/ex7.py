class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        if isinstance(other, Vector):
            return Vector(self.x + other.x, self.y + other.y)
        return NotImplemented

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

# Example usage:
v1 = Vector(2, 3)
v2 = Vector(4, 5)
v3 = v1 + v2

print(v3)  # Output: Vector(6, 8)

'''
In this example:

The Vector class has an __init__ method to initialize the x and y coordinates.
The __add__ method is defined to handle the addition of two Vector instances.
It checks if the other operand is also a Vector and returns a new Vector with the summed coordinates.
The __repr__ method is overridden to provide a readable string representation of the Vector objects.

This allows you to use the + operator with Vector instances in a natural and intuitive way.'
'''