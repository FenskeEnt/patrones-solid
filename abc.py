from abc import ABC, abstractmethod

class Animal(ABC):

    @abstractmethod
    def comer(self): pass

    @abstractmethod
    def caminar(self): ...

    @abstractmethod
    def dormir(self):
        """"""

class Persona(Animal):

    #overwriting
    def comer(self):
        return super().comer()

    def caminar(self):
        return super().caminar()

    def dormir(self):
        return super().dormir()

class Perro(Animal):

    def comer(self):
        return super().comer()

    def caminar(self):
        return super().caminar()

    def dormir(self):
        return super().dormir()


