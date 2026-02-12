import math

#Incremental development
#step 1: start with skeleton

#def area(radius):
#    """Calculate the area of a circle."""
#    return math.pi * radius ** 2

#step 2: add intermediate calculations

#def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    print(f"dx = {dx}, dy = {dy}")  # temporary
#    return 0.0

#step 3: complete the function

#def distance(x1, y1, x2, y2):
#    dx = x2 - x1
#    dy = y2 - y1
#    return (dx**2 + dy**2) ** 0.5


#Decomposition
#def circle_area(radius):
#    import math
#    return math.pi * radius ** 2

#def ring_area(outer, inner):
#    """Area of a ring (donut shape)."""
#    return circle_area(outer) - circle_area(inner)
#ring_area(5, 3)  # area between radius 5 and radius 3


#Boolean
def is_even(n):
    """Check if n is an even number."""
    return n % 2 == 0
is_even(4)   # True
is_even(7)   # False
is_even(3)

