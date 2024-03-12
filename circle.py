from __future__ import annotations
import math


class Circle:

    def __init__(self, radius):
        """Initialize a circle with given radius.
        
        :param radius: radius of the circle, may be zero.
        """
        if radius < 0:
            raise ValueError("radius must be non-negative")
        self.radius = radius

    def add_area(self, circle: Circle) -> Circle:
        """Return a new circle whose area equals the combined
        area of this circle and another circle.
        Since area is pi*r**2, the radii of the 3 circles
        should form a Pythagorean triple (r1^2 + r2^2 = r3^2)
        >>> circle0 = Circle(0)
        >>> circle3 = Circle(3)
        >>> circle4 = Circle(4)
        >>> circle5 = circle3.add_area(circle4)
        >>> circle5.get_radius() == 5
        True
        >>> circle_negative_rad = Circle(-1)
        Traceback (most recent call last):
        ...
        ValueError: radius must be non-negative
        >>> new_circle = circle3.add_area(circle0)
        >>> new_circle.get_radius() == circle3.get_radius()
        True
        """
        r1 = self.get_radius()
        r2 = circle.get_radius()
        # this is important, so show the operation in a rounded-box
        # on the Circle lifeline, or show it as a comment.
        r = math.hypot(r1, r2)
        # In a sequence diagram create a name for the new circle
        # so that you can show what is being returned.
        return Circle(r)

    def get_area(self) -> float:
        return math.pi*self.radius*self.radius
    
    def get_radius(self) -> float:
        return self.radius

    def __str__(self) -> str:
        return f"Circle({self.radius})"
    
    __repr__ = __str__


# if __name__ == "__main__":
#     c = Circle(-1)