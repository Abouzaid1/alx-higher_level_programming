
def display(width, height):
    """Display a rectangle of the given width and height."""
    for i in range(height):
        row = ""
        for j in range(width):
            row += "#"
        print(row)

display(1, 2)