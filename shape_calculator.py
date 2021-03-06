class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __str__(self):
        return "Rectangle(width=" + str(self.width) + ", height=" + str(
            self.height) + ")"

    def set_height(self, height):
        self.height = height

    def set_width(self, width):
        self.width = width

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return (self.width * 2) + (self.height * 2)

    def get_diagonal(self):
        return ((self.width**2) + (self.height**2))**.5

    def get_picture(self):
        if self.width > 50 or self.height > 50:
            return "Too big for picture."

        string = ""
        for _ in range(self.height):
            string += "*" * self.width + "\n"

        return string

    def get_amount_inside(self, rect):
        return int(self.width / rect.width) * int(self.height / rect.height)


class Square(Rectangle):
    def __init__(self, side):
        self.height = side
        self.width = side

    def __str__(self):
        return "Square(side=" + str(self.width) + ")"

    def set_side(self, side):
        self.height = side
        self.width = side