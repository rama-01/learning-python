from math import sqrt


class Triangle(object):
    def __init__(self, a, b, c):
        self._a = a
        self._b = b
        self._c = c

    # 类方法，或称为静态方法
    @staticmethod
    def is_valid(a, b, c):
        return a + b > c and a + c > b and b + c > a

    def perimeter(self):
        return self._a + self._b + self._c

    def area(self):
        p = self.perimeter() / 2
        return sqrt(p * (p - self._a) * (p - self._b) * (p - self._c))


def main():
    if Triangle.is_valid(3, 4, 5):
        t = Triangle(3, 4, 5)
        print(t.perimeter())
        print(t.area())
    else:
        print('cannot construct triangle')


if __name__ == '__main__':
    main()
