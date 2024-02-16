
def display(width, height, x, y):
    """Display a rectangle of the given width and height."""
    print("s\n" * y ,end="")
    for i in range(height):
        print("" * x ,"#" * width)


display(3, 2, 1, 4)
