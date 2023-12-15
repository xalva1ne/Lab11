
class Point:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Точка ({self.number})"


class Line:
    def __init__(self, start_point, end_point):
        self.start_point = Point(start_point)
        self.end_point = Point(end_point)

    def length(self):
        length = self.end_point.number - self.start_point.number
        if length < 0:
            length = -length
        return length

    def __str__(self):
        return f"Отрезок ({self.start_point.number}, {self.end_point.number}), Длинна: {self.length()}"


class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.side1 = Line(x1, y1)
        self.side2 = Line(x2, y2)
        self.side3 = Line(x3, y3)

    def perimeter(self):
        perimeter = self.side1.length() + self.side2.length() + self.side3.length()
        return perimeter

    def __str__(self):
        return f"Треугольник из отрезков ({self.side1}, {self.side2}, {self.side3}), Периметр: {self.perimeter()}"


# Пример использования:
point_A = Point(2)
point_B = Point(6)

line = Line(4, 3)
triangle = Triangle(5, 3, 2, 1, 6, 4)

print(point_A)
print(point_B)
print(line)
print(triangle)
