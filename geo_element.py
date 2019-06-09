# geometric calculation fx
def cramer(a, b, c, a1, b1, c1):
    a = float(a)
    b = float(b)
    c = float(c)
    a1 = float(a1)
    b1 = float(b1)
    c1 = float(c1)
    d = a * b1 - b * a1
    dx = a * c1 - c * a1
    dy = c * b1 - b * c1
    if d != 0:
        x = dx / d
        y = dy / d
        return (x, y)
    if d == 0:
        if dx != 0 or dy != 0:
            return "impossible"
        if dx == 0 and dy == 0:
            return "indeterminated"


def two_points_m(point1, point2):
    try:
        m = (point1.y - point2.y) / (point1.x - point2.x)
        return m
    except ZeroDivisionError:
        m = None
        return m


def perpendicular_m(m):
    try:
        return - 1.0/m
    except ZeroDivisionError:
        return None
    except TypeError:
        return 0

class Point:

    def __init__(self, x, y):
        self.x = float(x)
        self.y = float(y)


class Line:

    def __init__(self):
        self.m = None
        self.q = None

    def for_2_points(self, point1, point2):
        self.point1 = point1
        self.point2 = point2

        self.m = two_points_m(self.point1, self.point2)
        if self.m is None:
            self.q = self.point1.x
        else:
            self.q = - (self.m * self.point1.x) + self.point1.y

    def parallel(self, line_from_prl, point_prl):
        self.line_from_prl = line_from_prl
        self.point_prl = point_prl
        self.m = self.line_from_prl.m
        if self.m is None:
            self.q = self.point_prl.x
        else:
            self.q = - (self.line_from_prl.m * self.point_prl.x )+ self.point_prl.y

    def perpendicular(self, line_from_ppd, point_ppd):
        self.line_from_ppd = line_from_ppd
        self.point_ppd = point_ppd
        self.m = perpendicular_m(self.line_from_ppd.m)
        if self.m is None:
            self.q = self.point_ppd.x
        else:
            self.q = - (self.line_from_ppd.m * self.point_ppd.x )+ self.point_ppd.y

