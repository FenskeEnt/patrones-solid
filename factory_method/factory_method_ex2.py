from abc import ABC, abstractmethod

class IShape(ABC):

    @abstractmethod
    def area(self) -> int: pass

class Triangle(IShape):

    def __init__(self, width: int, heigh: int):
        self.width = width
        self.heigh = heigh

    def area(self) -> int:
        return (self.width * self.heigh) / 2

class Rectangle(IShape):

    def __init__(self, width: int, heigh: int):
        self.width = width
        self.heigh = heigh

    def area(self) -> int:
        return self.width * self.heigh

class Circle(IShape):

    def __init__(self, radio: int):
        self.radio = radio

    def area(self) -> int:
        return (3.14 * (self.radio)**2)


class IShapeFactory(ABC):

    @abstractmethod
    def get_shape(self) -> IShape: pass

class RectangleFactory(IShapeFactory):

    def get_shape(self, width: int, heigh: int) -> IShape:
        return Rectangle(width=width, heigh=heigh)

class TriangleFactory(IShapeFactory):

    def get_shape(self, width: int, heigh: int) -> IShape:
        return Triangle(width=width, heigh=heigh)

class CircleFactory(IShapeFactory):

    def get_shape(self, radio: int) -> IShape:
        return Circle(radio=radio)

class AreaCalculator:

    @staticmethod
    def calc_area(shape: IShapeFactory, *args):
        """Calcular el area de una figura espesifica"""
        shape = shape().get_shape(*args)
        area = shape.area()
        return area

def read_factory() -> IShapeFactory:
    factories = {
        'rectangulo': RectangleFactory,
        'triangulo': TriangleFactory,
        'circulo': CircleFactory
    }

    while True:
        option = str(input('Ingrese la opcion que desea calcular (rectangulo, triangulo, circulo): '))
        if option in factories:
            return factories[option]
        print(f'Opcion no valida: {option}')

if __name__ == '__main__':
    factory = read_factory()
    a = AreaCalculator.calc_area(factory, 20)
    print(a)