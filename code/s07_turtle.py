import turtle

def draw_square(turtle_obj, size=100):
    """draw a square with the given size"""
    for _ in range(4):
        turtle_obj.forward(size)
        turtle_obj.right(90)

def draw_spiral(t):
    """
    draw one square, turn an angle, then draw anothr square and so on
    """
    for i in range(36):
        draw_square(t, 50)
        t.left(10)

def main():
    t = turtle.Turtle()
    t.speed(5)
    draw_square(t)
    draw_square(t, size=50)
    turtle.mainloop()

if __name__ == "__main__":
    main()


