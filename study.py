
def display(width, height, x, y):
    """Display a rectangle of the given width and height."""
    print("s\n" * y ,end="")
    for i in range(height):
        print("" * x ,"#" * width)


display(3, 2, 1, 4)

# print("\n" * self.__y ,end="")
#         for i in range(self.__height):
#             print(" " * self.__x ,"#" * self.__width, end="")