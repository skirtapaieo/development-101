
import math

class Polygon:
    def get_sides(self):
        raise NotImplementedError

    def get_area(self):
        raise NotImplementedError

    def get_perimeter(self):
        return sum(self.get_sides())


class Triangle(Polygon):
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    def get_sides(self):
        return self.sides

    def get_area(self):
        return self._get_triangle_area()

    def _get_triangle_area(self):
        side1, side2, side3 = self.sides
        semi_perimeter = (side1 + side2 + side3) / 2
        return math.sqrt(semi_perimeter * (semi_perimeter - side1) * (semi_perimeter - side2) * (semi_perimeter - side3))

    # Original area calculation, moved into the class as a private method
    # def get_area(self):
    #     side1, side2, side3 = self.sides
    #     return get_triangle_area(side1, side2, side3)


class Rectangle(Polygon):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_sides(self):
        return [self.width, self.height, self.width, self.height]

    def get_area(self):
        return self._get_rectangle_area()

    def _get_rectangle_area(self):
        return self.width * self.height

    # Original area calculation, moved into the class as a private method
    # def get_area(self):
    #     return get_rectangle_area(self.width, self.height)


class Square(Rectangle):
    def __init__(self, side_length):
        super().__init__(side_length, side_length)

# The following code is now unnecessary because the logic has been moved into the classes
# def get_triangle_area(side1, side2, side3):
#     semi_perimeter = (side1 + side2 + side3) / 2
#     return math.sqrt(
#         semi_perimeter *
#         (semi_perimeter - side1) *
#         (semi_perimeter - side2) *
#         (semi_perimeter - side3)
#     )

# def get_rectangle_area(width, height):
#     return width * height
