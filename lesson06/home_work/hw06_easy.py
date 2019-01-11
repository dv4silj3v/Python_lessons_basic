# Задача-1: Написать класс для фигуры-треугольника, заданного координатами трех точек.
# Определить методы, позволяющие вычислить: площадь, высоту и периметр фигуры.

import math


class Triangle:
    def __init__(self, ax, ay, bx, by, cx, cy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy

    def calc_side_length(self):
        """
        Calculate triangle side length
        """
        side_length = []
        side_length.append(math.sqrt((self.ax - self.bx) ** 2 + (self.ay - self.by) ** 2))
        side_length.append(math.sqrt((self.ax - self.cx) ** 2 + (self.ay - self.cy) ** 2))
        side_length.append(math.sqrt((self.bx - self.cx) ** 2 + (self.by - self.cy) ** 2))
        return side_length

    def calc_perimeter(self):
        """
        Calculate triangle perimeter.
        """
        p = self.calc_side_length()[0] + self.calc_side_length()[1] + self.calc_side_length()[2]
        return p

    def calc_area(self):
        """
        Calculate area of a triangle.
        """
        half_p = self.calc_perimeter()/2
        area = math.sqrt(half_p * (half_p - self.calc_side_length()[0]) * (half_p - self.calc_side_length()[1]) * (half_p - self.calc_side_length()[2]))
        return area

    def calc_height(self):
        """
        Calculate heights of a triangle.
        """
        height_ab = 2 * (self.calc_area() / self.calc_side_length()[0])
        height_ac = 2 * (self.calc_area() / self.calc_side_length()[1])
        height_bc = 2 * (self.calc_area() / self.calc_side_length()[2])
        return height_ab, height_ac, height_bc


triangle1 = Triangle(2, 4, 34, -23, 23, 0)
print("Side lengths of a triangle are:",triangle1.calc_side_length())
print("Perimeter of a triangle is:",triangle1.calc_perimeter())
print("Area of a triangle is:",triangle1.calc_area())
print("Heights of a triangle are:",triangle1.calc_height())


# Задача-2: Написать Класс "Равнобочная трапеция", заданной координатами 4-х точек.
# Предусмотреть в классе методы:
# проверка, является ли фигура равнобочной трапецией;
# вычисления: длины сторон, периметр, площадь.


class IsoscelesTrapezoid:
    def __init__(self, ax, ay, bx, by, cx, cy, dx, dy):
        self.ax = ax
        self.ay = ay
        self.bx = bx
        self.by = by
        self.cx = cx
        self.cy = cy
        self.dx = dx
        self.dy = dy

    def Isosceles_check(self):
        """
        Checks if trapezoid is isosceles
        """
        diag_length = []
        diag_length.append((math.sqrt((self.ax - self.cx) ** 2 + (self.ay - self.cy) ** 2)))
        diag_length.append((math.sqrt((self.bx - self.dx) ** 2 + (self.ay - self.cy) ** 2)))
        if diag_length[0] == diag_length[1]:
            return True
        else:
            return False

    def calc_side_length(self):
        """
        Calculate isosceles trapezoid lenght of sides
        """
        if self.Isosceles_check():
            side_length = []
            side_length.append(math.sqrt((self.ax - self.bx) ** 2 + (self.ay - self.by) ** 2))
            side_length.append(math.sqrt((self.bx - self.cx) ** 2 + (self.by - self.cy) ** 2))
            side_length.append(math.sqrt((self.cx - self.dx) ** 2 + (self.cy - self.dy) ** 2))
            side_length.append(math.sqrt((self.ax - self.dx) ** 2 + (self.ay - self.dy) ** 2))
            return side_length
        else:
            print("Incorrect input, trapezoid is NOT isosceles")

    def calc_perimeter(self):
        """
        Calculate perimeter of a isosceles trapezoid
        """
        p = (2 * self.calc_side_length()[0]) + self.calc_side_length()[1] + self.calc_side_length()[3]
        return p

    def calc_height(self):
        """
        Calculate height of a isosceles trapezoid
        """
        height = (math.sqrt(4 * (self.calc_side_length()[0]) ** 2 - (self.calc_side_length()[1] - self.calc_side_length()[3]))) / 2
        return height

    def calc_area(self):
        """
        Calculate area of a isosceles trapezoid
        """
        area = self.calc_height() * (self.calc_side_length()[1] + self.calc_side_length()[3]) / 2
        return area


trapezoid1 = IsoscelesTrapezoid(0, 0, 1, 4, 7, 4, 8, 0)

print("Side lengths of a trapezoid are:",trapezoid1.calc_side_length())
print("Perimeter of a trapezoid is:",trapezoid1.calc_perimeter())
print("Area of a trapezoid is:",trapezoid1.calc_area())







