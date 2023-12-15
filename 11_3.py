
class Point:
    def __init__(self, number):
        self.number = number

    def __str__(self):
        return f"Точка ({self.number})"

    def __add__(self, other):
        # Перегрузка оператора сложения для класса Point
        if isinstance(other, Point):
            return Point(self.number + other.number)
        else:
            raise TypeError("Нельзя сложить точку с объектом другого типа.")


point_A = Point(2)
point_B = Point(6)
point_C = point_A + point_B

print(point_A)
print(point_B)
print(point_C)

